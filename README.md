# A Novel Any-angle 2D MTF Estimation for Single Satellite Image Super-Resolution
## 1. Python Supported
### 1.1. Version
1. GDAL--3.4.3
2. opencv-python--4.8.0.76
3. pylsd--0.0.3
4. pandas--1.5.2
5. numpy--1.24.4
6. scipy--1.10.1
7. matplotlib--3.7.0
8. scikit-image--0.20.0
##
1. Step one: Automaticly extract edge-objects with any-angle. Automatic_Any_Angle_Roi_Selection.py
2. Step Two: Calculate 1D MTF of each edge-object with any-angle. Calculate_1D_MTF.py
3. Step Three: Use two demisional Gaussian function to estimate 2D MTF. Fit_Gaussian_2D_MTF.py
4. Step Four: Perform SSIR on single satellite scene image. Image_MTF_SSIR.py
5. Step Five: SSIR_Assessment.py


**The advantages of Our Method are that not only can directly perform SSIR on single satellite scene image but also can retain origin radiometric information as much as possible.**

## 2. Results Presentation

## 2.1. LR & HR

HR is corrected by our methods.

[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/airport_compare_new.png?raw=true" width="500px">](https://imgsli.com/MjE1ODkz)

[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/Urban_new.png?raw=true" width="500px">](https://imgsli.com/MjE1OTk0)

[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/parkinglot_compare.png?raw=true" width="500px">](https://imgsli.com/MjE1NzI2)

### 2.2. SSIR Iteration Process Results of Using Newton's method (LR to HR)

<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/airplane_GiF.gif?raw=true" width="500px">

![sparseresidential_gif](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/sparseresidential_gif.gif?raw=true)

## 3. More Comparison Results
More qualitative and quantitative comparison results on SDGSAT-1 satellite and public datasets (Ucmerced dataset, WHU-RS19 dataset, and RSSCN7 dataset) are shown as follows. `/` denotes that the result is distorted.

### 3.1. SDGSAT-1 Satellite

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/SDGSAT-1_compare_new.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/SDGSAT-1_comparex.png?raw=true)

### 3.2. UCMerced Dataset

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/airplane51.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/airplane51x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/beach75.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/beach75x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/beach85.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/beach85x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/chaparral66.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/chaparral66x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/parkinglot50.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/parkinglot50x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/sparseresidential99.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/sparseresidential99x.png?raw=true)

### 3.3. WHU-RS19 Dataset

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/Desert_20.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/Desert_20x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/river_21.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/river_21x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/Mountain_01.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/Mountain_01x.png?raw=true)

### 3.4. RSSCN7 Dataset

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/e251.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/e251x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/e273.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/e273x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/g246.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/g246x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/g297.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/g297x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/g391.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/g391x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/g392.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/g392x.png?raw=true)



