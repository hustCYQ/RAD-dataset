# RAD: A Comprehensive Dataset for Benchmarking the Robustness of Image Anomaly Detection

Yuqi Cheng, Yunkang Cao, Rui Chen, Weiming Shen*

(*Corresponding authors)

Our paper has been accepted by CASE 2024 [[Paper]](https://arxiv.org/abs/2406.07176)

# Overview
This study introduces a Robust Anomaly Detection (RAD) dataset with **free views, uneven illuminations, and blurry collections** to systematically evaluate the **robustness** of current anomaly detection methods.


# RAD

<img src="./img/fig4.png" width=900 alt="Real3D Dataset" align=center>


## Summary
+ overview of all classes in Real3D-AD

Real3D-AD comprises a total of 1,254 samples that are distributed across 12 distinct categories. These categories include Airplane, Car, Candybar, Chicken, Diamond, Duck, Fish, Gemstone, Seahorse, Shell, Starfish, and Toffees.


## Download

+ To download the Real3D-AD dataset (Dataset for training and evaluation, pcd format), click [real3d-ad-pcd.zip(google drive)](https://drive.google.com/file/d/1oM4qjhlIMsQc_wiFIFIVBvuuR8nyk2k0/view?usp=sharing) or [real3d-ad-pcd.zip(baidu disk: vrmi)](https://pan.baidu.com/s/1orQY3DjR6Z0wazMNPysShQ)
+ To download the Real3D-AD dataset (Source data from camera, ply format), click [real3d-ad-ply.zip(google drive)](https://drive.google.com/file/d/1lHjvyVquuO8-ROOYcnf7O_lliL1Wa36V/view?usp=sharing) or [real3d-ad-ply.zip(baidu disk：vvz1)](https://pan.baidu.com/s/1BRdJ8oSwrpAPxTOEwUrjdw)


### Data preparation
- Download real3d-ad-pcd.zip and extract into `./data/`
```
data
├── airplane
    ├── train
        ├── 1_prototype.pcd
        ├── 2_prototype.pcd
        ...
    ├── test
        ├── 1_bulge.pcd
        ├── 2_sink.pcd
        ...
    ├── gt
        ├── 1_bulge.txt
        ├── 2_sink.txt
        ... 
├── car
...
```



## Dataset Statistic

+ brief describe our dataset in Table
  
| Source | Class         | Real Size [mm] (length/width/height) | Transparency | TrainingNum (good) | TestNum (good) | TestNum (defect) | TotalNum | TrainingPoints (min/max/mean) | TestPoints (min/max/mean) | AnomalyProportion Δ |
|:--------:|---------------|----------------------------:|--------------:|-----------------:|-------------:|---------------:|-------:|----------------------------:|---------------------------:|--------:|
| 1      | Airplane      |     34.0/14.2/31.7         |      Yes     |               4 |          50 |            50 |   104 |       383k/ 413k/ 400k     |       168k/ 773k/351k     |  1.17% |
| 2      | Car           |     35.0/29.0/12.5         |      Yes     |               4 |          50 |            50 |   104 |       566k/1296k/1097k     |        90k/ 149k/131k     |  1.98% |
| 3      | Candybar      |     33.0/20.0/ 8.0         |      Yes     |               4 |          50 |            50 |   104 |       339k/1183k/ 553k     |       149k/ 180k/157k     |  2.36% |
| 4      | Chicken       |     25.0/14.0/20.0         | No (white)   |               4 |          52 |            54 |   110 |       217k/1631k/1157k     |        87k/1645k/356k     |  4.46% |
| 5      | Diamond       |     29.0/29.0/18.7         |      Yes     |               4 |          50 |            50 |   104 |      1477k/2146k/1972k     |        66k/  84k/ 75k     |  5.40% |
| 6      | Duck          |     30.0/22.2/29.4         |      Yes     |               4 |          50 |            50 |   104 |       545k/2675k/1750k     |       155k/ 784k/216k     |  1.99% |
| 7      | Fish          |     37.7/24.0/ 4.0         |      Yes     |               4 |          50 |            50 |   104 |       230k/ 251k/ 240k     |       104k/ 117k/110k     |  2.85% |
| 8      | Gemstone      |     22.5/18.8/17.0         |      Yes     |               4 |          50 |            50 |   104 |       169k/1819k/ 835k     |        43k/ 645k/104k     |  2.06% |
| 9      | Seahorse      |     38.0/11.2/ 3.5         |      Yes     |               4 |          50 |            50 |   104 |       189k/ 203k/ 194k     |        74k/  90k/ 83k     |  4.57% |
| 10     | Shell         |     21.7/22.0/ 7.7         |      Yes     |               4 |          52 |            48 |   104 |       280k/ 316k/ 295k     |       110k/ 144k/125k     |  2.25% |
| 11     | Starfish      |     27.4/27.4/ 4.8         |      Yes     |               4 |          50 |            50 |   104 |       198k/ 209k/ 202k     |        74k/ 116k/ 88k     |  4.46% |
| 12     | Toffees       |     38.0/12.0/10.0         |      Yes     |               4 |          50 |            50 |   104 |       178k/1001k/ 385k     |        78k/  97k/ 88k     |  2.46% |

(Δ: Mean proportion of abnormal point clouds in Test set)

## Data Collection

+ description of instruments

<img src="./doc/instruments.png" width=300 alt="instruments" align=center>
The PMAX-S130 optical system comprises a pair of lenses with low distortion properties, a high luminance LED, and a blue-ray filter. The blue light scanner is equipped with a lens filter that selectively allows only the blue light of a specific wavelength to pass through. The filter effectively screens the majority of blue light due to its relatively low concentration in both natural and artificial lighting. Nevertheless, using blue light-emitting light sources could pose a unique obstacle in this context. The image sensor can collect light using the lens aperture. Hence, the influence exerted by ambient light is vastly reduced.

+ how to capture point clouds and complete one prototype

<img src="./doc/make_prototypes.png" width=900 alt="make prototype" align=center>
Initially, the stationary object undergoes scanning while the turntable completes a full revolution of 360°, enabling the scanner to capture images of the various facets of the object. Subsequently, the object undergoes reversal, and the process of rotation and scanning is reiterated. Following the manual calibration of the front and back scanning outcomes, the algorithm performs a precise calibration of the stitching process. If there are any gaps in the stitching outcome, the scan stitching process is reiterated until the point cloud is rendered.

+ anomalies

The anomalies pertaining to point clouds can be classified into two categories: incompleteness and redundancy. In the dataset, we named them bulge and sink. Besides, more samples are made by copying and cutting edges.


## Annotation
+ how to annotate

The collected point clouds are annotated using CloudCompare software
CloudCompare is a 3D point cloud (grid) editing and processing software. Originally, it was designed to directly compare dense three-dimensional point clouds. It relies on a specific octree structure and provides excellent performance for tasks such as point cloud comparison.
The anotation process of point cloud is shown in the figure below.
<!-- ![image-20230605141032952](https://github.com/M-3LAB/H3D-AD/blob/main/doc/anotation.png) -->

<img src="./doc/annotation.png" width=900 alt="Anotation phase" align=center>

## Benchmark

+ beseline methods
  
We take BTF and M3DM as basic baseline methods, and improve baseline using PatchCore.

+ metrics
  
We choose AUROC and AUPU as metric for object level and point level anomaly detection.

+ benchmark results

### Other methods on Real3D-AD

Complementary Pseudo Multimodal Feature for Point Cloud Anomaly Detection [[paper 2023]](https://arxiv.org/abs/2303.13194)[[code]](https://github.com/caoyunkang/CPMF)
Towards Scalable 3D Anomaly Detection and Localization: A Benchmark via 3D Anomaly Synthesis and A Self-Supervised Learning Network [[paper 2023]](https://arxiv.org/abs/2311.14897)[[code]](https://github.com/Chopper-233/Anomaly-ShapeNet)
+ PointCore: Efficient Unsupervised Point Cloud Anomaly Detector Using Local-Global Features [[paper 2024]](https://arxiv.org/abs/2403.01804)

|          | Object AUROC | Point AUROC | Max F1 Point | Point AP |
|----------|------------|-----------|--------------|----------|
| airplane | 0.632      | 0.618     | 0.023        | 0.010    |
| candybar | 0.518      | 0.836     | 0.135        | 0.064    |
| car      | 0.718      | 0.734     | 0.107        | 0.050    |
| chicken  | 0.640      | 0.559     | 0.071        | 0.031    |
| diamond  | 0.640      | 0.753     | 0.149        | 0.074    |
| duck     | 0.554      | 0.719     | 0.042        | 0.018    |
| fish     | 0.840      | 0.988     | 0.582        | 0.559    |
| gemstone | 0.349      | 0.449     | 0.020        | 0.007    |
| seahorse | 0.843      | 0.962     | 0.615        | 0.636    |
| shell    | 0.393      | 0.725     | 0.052        | 0.025    |
| starfish | 0.526      | 0.800     | 0.202        | 0.128    |
| toffees  | 0.845      | 0.959     | 0.460        | 0.391    |
| MEAN     | 0.625      | 0.758     | 0.205        | 0.166    |

Towards Scalable 3D Anomaly Detection and Localization: A Benchmark via 3D Anomaly Synthesis and A Self-Supervised Learning Network [[paper]](https://arxiv.org/abs/2311.14897)[[code]](https://github.com/Chopper-233/Anomaly-ShapeNet)


### The 3D anomaly detection performance when using 4 prototypes for training.


## Acknowledgments.
This work is supported by the National Key R&D Program of China (Grant NO. 2022YFF1202903) and the National Natural Science Foundation of China (Grant NO. 62122035, 62206122).

Our benchmark is built on [BTF](https://github.com/eliahuhorwitz/3D-ADS) and [M3DM](https://github.com/nomewang/M3DM) and [PatchCore](https://github.com/amazon-science/patchcore-inspection), thanks their extraordinary works!

Thanks to all the people who worked hard to capture the data, especially Xinyu Tang for his efforts.

## License
The dataset is released under the CC BY 4.0 license.

## BibTex Citation

If you find this paper and repository useful, please cite our paper☺️.

```
@inproceedings{liu2023real3d,
  title={Real3D-AD: A Dataset of Point Cloud Anomaly Detection},
  author={Liu, Jiaqi and Xie, Guoyang and Li, Xinpeng and Wang, Jinbao and Liu, Yong and Wang, Chengjie and Zheng, Feng and others},
  booktitle={Thirty-seventh Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
  year={2023}
}
```
