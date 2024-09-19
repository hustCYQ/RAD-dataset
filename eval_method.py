from sklearn.metrics import auc, roc_auc_score, average_precision_score, f1_score, precision_recall_curve, pairwise
from skimage import measure
import numpy as np
import cv2
import os


def normalize(pred, max_value=None, min_value=None):
    if max_value is None or min_value is None:
        return (pred - pred.min()) / (pred.max() - pred.min())
    else:
        return (pred - min_value) / (max_value - min_value)


def apply_ad_scoremap(image, scoremap, alpha=0.5):
    np_image = np.asarray(image, dtype=float)
    scoremap = (scoremap * 255).astype(np.uint8)
    scoremap = cv2.applyColorMap(scoremap, cv2.COLORMAP_JET)
    scoremap = cv2.cvtColor(scoremap, cv2.COLOR_BGR2RGB)
    return (alpha * np_image + (1 - alpha) * scoremap).astype(np.uint8)





def cal_pro_score(masks, amaps, max_step=200, expect_fpr=0.3):
    # ref: https://github.com/gudovskiy/cflow-ad/blob/master/train.py
    binary_amaps = np.zeros_like(amaps, dtype=bool)
    min_th, max_th = amaps.min(), amaps.max()
    delta = (max_th - min_th) / max_step
    pros, fprs, ths = [], [], []
    for th in np.arange(min_th, max_th, delta):
        binary_amaps[amaps <= th], binary_amaps[amaps > th] = 0, 1
        pro = []
        for binary_amap, mask in zip(binary_amaps, masks):
            for region in measure.regionprops(measure.label(mask)):
                tp_pixels = binary_amap[region.coords[:, 0], region.coords[:, 1]].sum()
                pro.append(tp_pixels / region.area)
        inverse_masks = 1 - masks
        fp_pixels = np.logical_and(inverse_masks, binary_amaps).sum()
        fpr = fp_pixels / inverse_masks.sum()
        pros.append(np.array(pro).mean())
        fprs.append(fpr)
        ths.append(th)
    pros, fprs, ths = np.array(pros), np.array(fprs), np.array(ths)
    idxes = fprs < expect_fpr
    fprs = fprs[idxes]
    if len(fprs)>0:
        fprs = (fprs - fprs.min()) / (fprs.max() - fprs.min())
        pro_auc = auc(fprs, pros[idxes])
    else:
        pro_auc = 0
    return pro_auc



def cal_all_scores(gt_list_sp,pr_list_sp,gt_list_px,pr_list_px):

    # auroc
    auroc_sp = roc_auc_score(gt_list_sp, pr_list_sp)
    auroc_px = roc_auc_score(gt_list_px.ravel(), pr_list_px.ravel())
    
    # AP
    ap_sp = average_precision_score(gt_list_sp, pr_list_sp)
    ap_px = average_precision_score(gt_list_px.ravel(), pr_list_px.ravel())
    # f1_sp
    precisions, recalls, thresholds = precision_recall_curve(gt_list_sp, pr_list_sp)
    f1_scores = (2 * precisions * recalls) / (precisions + recalls)
    f1_sp = np.max(f1_scores[np.isfinite(f1_scores)])
    # f1_px
    precisions, recalls, thresholds = precision_recall_curve(gt_list_px.ravel(), pr_list_px.ravel())
    f1_scores = (2 * precisions * recalls) / (precisions + recalls)
    f1_px = np.max(f1_scores[np.isfinite(f1_scores)])
    # aupro
    if len(gt_list_px.shape) == 4:
        gt_list_px = gt_list_px.squeeze(1)
    if len(pr_list_px.shape) == 4:
        pr_list_px = pr_list_px.squeeze(1)
    aupro = cal_pro_score(gt_list_px, pr_list_px)

    # auroc_px = round(roc_auc_score(gt_list_px, pr_list_px), 3)
    # auroc_sp = round(roc_auc_score(gt_list_sp, pr_list_sp), 3)

    auroc_sp = round(auroc_sp,3)
    auroc_px = round(auroc_px,3)
    ap_sp = round(ap_sp,3)
    ap_px = round(ap_px,3)
    f1_sp = round(f1_sp,3)
    f1_px = round(f1_px,3)
    aupro = round(aupro,3)

    return auroc_sp,auroc_px,ap_sp,ap_px,f1_sp,f1_px,aupro