# Any-angle 2D MTF Estimation for Single Satellite Image Sharpening
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
1. Step one: Automaticly extract edge objects with any-angle. Automatic_Any_Angle_Roi_Selection.py
2. Step Two: Calculate 1D MTF of each edge object with any-angle. Calculate_1D_MTF_RANSAC.py
3. Step Three: Use two demisional Gaussian function to estimate 2D MTF. Fit_Gaussian_2D_MTF.py
4. Step Four: Perform Sharpening on single satellite scene image. Image_MTF_Sharpen.py
5. Step Five: Assessment.py

**The advantages of Our Method are following aspects:**

**(1) Efficiency: It can directly perform sharpening and SISR on single satellite scene image with superior speed.** 

**(2) Parameter Setting: It only needs to set one adjustable parameter in the proposed method.**

**(3) Preservation: It can preserve origin radiometric information as much as possible.**

**(4) Automation: It fulfills the automatic sharpening process during the radiometic correction of raw satellite images in the satellite ground station.**

## 2. Results Presentation

### 2.1. Raw Image & Ours

Ours is corrected by the proposed method.

[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/airport_compare_new.png?raw=true" width="500px">](https://imgsli.com/MjE5MDY1) 

[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/Urban_Compare.png?raw=true" width="500px">](https://imgsli.com/MjE5MDY3)

### 2.2. Iteration Process of Sharpening Results using Our method (LR to Sharpen)

<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/parkinglot_GIF_new.gif?raw=true" width="400px"> 

<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/airplane_GiF_new.gif?raw=true" width="400px">

## 3. Extended Applications on Single Image Super-Resolution (SISR)
More qualitative and quantitative comparison results on SDGSAT-1 satellite and public datasets (Ucmerced dataset, WHU-RS19 dataset, and RSSCN7 dataset) are shown as follows. `/` denotes that the result is distorted.

### 3.1. SDGSAT-1 Satellite

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/SDGSAT-1_water.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/SDGSAT-1_water_x.png?raw=true)

### 3.2. UCMerced Dataset

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/airplane51.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/airplane51_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/beach75.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/beach75_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/beach85.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/beach85_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/chaparral66.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/chaparral66_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/parkinglot50.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/parkinglot50_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/sparseresidential99.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/sparseresidential99_x.png?raw=true)

### 3.3. WHU-RS19 Dataset

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/Desert_20.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/Desert_20_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/river_21.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/river_21_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/Mountain_01.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/Mountain_01_x.png?raw=true)

### 3.4. RSSCN7 Dataset

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/e251.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/e251_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/e273.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/e273_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/g246.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/g246_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/g297.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/g297_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/g391.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/g391_x.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/g392.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Public%20Datasets/g392_x.png?raw=true)

## 4. Automatic Processing of Raw Images

The automated processing of 9 raw scene images captured over the course of one year using our proposed method can further validate the efficacy and automation of the generation process.

We also compare the super-resolution processing time for each raw scene image using different methods.

The results of some different ground objects extracted from 9 scene images are showcased:

### 4.1. Scene captured at 21/12/2022
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20221221/11_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU2) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20221221/6_3_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU1) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20221221/1_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU0)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing/Scene1.png?raw=true)

### 4.2. Scene captured at 11/01/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230111/3_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU3) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230111/3_6_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU4)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing/Scene2.png?raw=true)

### 4.3. Scene captured at 15/01/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230115/1_0_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU5) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230115/1_5_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTYw) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230115/8_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTYy)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing/Scene3.png?raw=true)

### 4.4. Scene captured at 30/03/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230330/0_6_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTc2) 

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing/Scene4.png?raw=true)

### 4.5. Scene captured at 07/05/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230507/0_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTY0) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230507/1_0_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTY1) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230507/8_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDI4) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230507/8_6_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDU5)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing/Scene5.png?raw=true)

### 4.6. Scene captured at 13/05/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230513/0_5_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTY4) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230513/15_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDIy) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230513/2_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTY5) 

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing/Scene6.png?raw=true)

### 4.7. Scene captured at 13/07/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230713/3_0_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTgw) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230713/3_1_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDI1) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230713/6_0_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTc0) 

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing/Scene7.png?raw=true)

### 4.8. Scene captured at 07/08/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230807/13_3_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDE5) 

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing/Scene8.png?raw=true)

### 4.9. Scene captured at 14/09/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230914/1_1_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDEy) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230914/14_3_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDE2) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230914/14_5_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDE1) 

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing/Scene9.png?raw=true)

