# Any-angle 2D MTF Estimation for Single Satellite Image Super-Resolution
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
4. Step Four: Perform SISR on single satellite scene image. Image_MTF_SISR.py
5. Step Five: SISR_Assessment.py


**The advantages of Our Method are that not only can directly perform SISR on single satellite scene image with superior speed but also can preserve origin radiometric information as much as possible.**

## 2. Results Presentation

### 2.1. Raw Image & Ours

Ours is corrected by the proposed method.

[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/airport_compare_new.png?raw=true" width="500px">](https://imgsli.com/MjE5MDY1) 

[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/Urban_Compare.png?raw=true" width="500px">](https://imgsli.com/MjE5MDY3)

### 2.2. Iteration Process of Sharpen Results using Our method (LR to Sharpen)

<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/parkinglot_GIF.gif?raw=true" width="400px"> 

<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/airplane_GiF_.gif?raw=true" width="400px">

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

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/parkinglot_.png?raw=true)
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

## 4. Automatic Processing of Raw Images

The automated processing of 9 raw scene images captured over the course of one year using our proposed method can further validate the generation.

The results of some different ground objects extracted from 9 scene images are showcased:

### 4.1. Scene captured at 21/12/2022
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20221221/11_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU2) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20221221/6_3_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU1) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20221221/1_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU0)

### 4.2. Scene captured at 11/01/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230111/3_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU3) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230111/3_6_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU4)

### 4.3. Scene captured at 15/01/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230115/1_0_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTU5) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230115/1_5_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTYw) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230115/8_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTYy)

### 4.4. Scene captured at 30/03/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230330/0_6_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTc2) 

### 4.5. Scene captured at 07/05/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230507/0_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTY0) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230507/1_0_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTY1) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230507/8_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDI4) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230507/8_6_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDU5)

### 4.6. Scene captured at 13/05/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230513/0_5_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTY4) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230513/15_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDIy) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230513/2_2_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTY5) 

### 4.7. Scene captured at 13/07/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230713/3_0_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTgw) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230713/3_1_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDI1) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230713/6_0_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE4OTc0) 

### 4.8. Scene captured at 07/08/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230807/13_3_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDE5) 

### 4.9. Scene captured at 14/09/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230914/1_1_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDEy) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230914/14_3_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDE2) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing/20230914/14_5_imgsli.png?raw=true" width="250px">](https://imgsli.com/MjE5MDE1) 

