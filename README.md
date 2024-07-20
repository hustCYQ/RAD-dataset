# RAD: A Comprehensive Dataset for Benchmarking the Robustness of Image Anomaly Detection

Yuqi Cheng, Yunkang Cao, Rui Chen, Weiming Shen*

(*Corresponding authors)

Our paper has been accepted by CASE 2024 [[Paper]](https://arxiv.org/abs/2406.07176)

# Overview
This study introduces a Robust Anomaly Detection (RAD) dataset with **free views, uneven illuminations, and blurry collections** to systematically evaluate the **robustness** of current anomaly detection methods.


# RAD

<img src="./img/fig4.png" width=900 alt="RAD Dataset" align=center>


## Summary
+ overview of all classes in Real3D-AD

Real3D-AD comprises a total of 1,254 samples that are distributed across 12 distinct categories. These categories include Airplane, Car, Candybar, Chicken, Diamond, Duck, Fish, Gemstone, Seahorse, Shell, Starfish, and Toffees.


## Download

+ To download the Real3D-AD dataset (Dataset for training and evaluation, pcd format), click [real3d-ad-pcd.zip(google drive)](https://drive.google.com/file/d/1oM4qjhlIMsQc_wiFIFIVBvuuR8nyk2k0/view?usp=sharing) or [real3d-ad-pcd.zip(baidu disk: vrmi)](https://pan.baidu.com/s/1orQY3DjR6Z0wazMNPysShQ)
+ To download the Real3D-AD dataset (Source data from camera, ply format), click [real3d-ad-ply.zip(google drive)](https://drive.google.com/file/d/1lHjvyVquuO8-ROOYcnf7O_lliL1Wa36V/view?usp=sharing) or [real3d-ad-ply.zip(baidu disk：vvz1)](https://pan.baidu.com/s/1BRdJ8oSwrpAPxTOEwUrjdw)


### Data Struct

```
RAD-dataset
├── bolt
    ├── train
        ├── good
    ├── test
        ├── good
        ├── defect
    ├── ground_truth
        ├── defect
├── ribbon
...
```



## Dataset Statistic

+ brief describe our dataset in Table 1.
  
<img src="./img/tab1.png" width=400 alt="RAD Dataset" align=center>


## Data Collection


<img src="./img/fig1.png" width=400 alt="instruments" align=center>


## Annotation


<img src="./img/fig3.png" width=400 alt="Anotation phase" align=center>

## Benchmark

+ beseline methods
  
We take BTF and M3DM as basic baseline methods, and improve baseline using PatchCore.

+ metrics
  
We choose AUROC and AUPU as metric for object level and point level anomaly detection.

+ benchmark results


<img src="./img/tab2.png" width=900 alt="image-wise" align=center>


<img src="./img/tab3.png" width=900 alt="pixel-wise" align=center>
<img src="./img/fig5.png" width=900 alt="vis" align=center>

## Acknowledgments.
Resrach supported by the Fundamental Research Funds for the Central Universities: HUST:2021GCRC058.


## License
The dataset is released under the CC BY 4.0 license.

## BibTex Citation

If you find this paper and repository useful, please cite our paper☺️.

```
@inproceedings{Cheng2024RAD,
  title={RAD: A Comprehensive Dataset for Benchmarking the Robustness of Image Anomaly Detection},
  author={Yuqi Cheng, Yunkang Cao, Rui Chen and Weiming Shen},
  booktitle={2024 IEEE 20th International Conference on Automation Science and Engineering},
  year={2024}
}
```
