#Single Satellite Image Sharpening with Any-angle 2D MTF Estimation
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
4. Step Four: Perform Sharpening/SSIR on single satellite scene image. Image_MTF_Sharpen_SISR.py
5. Step Five: Assessment.py

**The advantages of Our Method are following aspects:**

**(1) Efficiency: It can directly perform sharpening and SISR on a single satellite scene image, offering superior speed with minimal computational memory requirements.** 

**(2) Parameter Setting: It only has a single tunable parameter in the proposed method.**

**(3) Preservation: It effectively preserves origin radiometric information.**

**(4) Low complexity: It does not rely on HR images as reference.**

**(5) Reuse: One-time estimated 2D MTF can be repeatedly applied to various raw images for an extended duration.**

**(6) Automation: It fulfills the automatic sharpening/SISR process during the radiometic correction of raw satellite images in the Satellite Ground Station System.**

## 2. Sharpening Results Presentation

### 2.1. Raw Image & Ours

Ours is corrected by the proposed method.

[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/airport_compare_new.png?raw=true" width="500px">](https://imgsli.com/MjE5MDY1) 

[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/Urban_Compare.png?raw=true" width="500px">](https://imgsli.com/MjE5MDY3)

### 2.2. Iteration Process of Sharpening Results using Our method

<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/parkinglot_GIF_new.gif?raw=true" width="400px"> 

<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures/airplane_GiF_new.gif?raw=true" width="400px">

## 3. Extended Applications on Single Image Super-Resolution (SISR)
More qualitative and quantitative comparison results on public datasets (Ucmerced dataset, WHU-RS19 dataset, and RSSCN7 dataset) are shown as follows. `/` denotes that the result is distorted.

### 3.1. UCMerced Dataset

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/airplane51.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/airplane51_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/beach75.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/beach75_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/beach85.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/beach85_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/chaparral66.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/chaparral66_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/parkinglot50.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/parkinglot50_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/sparseresidential99.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/sparseresidential99_.png?raw=true)

### 3.2. WHU-RS19 Dataset

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/Desert_20.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/Desert_20_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/river_21.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/river_21_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/Mountain_01.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/Mountain_01_.png?raw=true)

### 3.3. RSSCN7 Dataset

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/e251.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/e251_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/e273.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/e273_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/g246.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/g246_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/g297.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/g297_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/g391.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/g391_.png?raw=true)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/g392.png?raw=true)
![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20pictures%20new/g392_.png?raw=true)

## 4. Reuse of One-time Estimation on Raw Images

The raw satellite images are without any radiometric or geometric correction. For a given sensor, imaging degradation remains fixed over a certain period, implying that the one-time estimated 2D MTF can be repeatedly applied to various raw images for an extended duration. We applied a 2D MTF estimated from one raw scene image to directly process 9 raw scene images captured by SDGSAT-1 over one year.

We also compare the super-resolution processing time for each raw scene image using different methods.

The results of some different ground objects extracted from 9 scene images are showcased:

### 4.1. Scene captured at 21/12/2022
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20221221/11_2_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxMzc2) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20221221/6_3_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxMzc1) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20221221/1_2_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxMzcy)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing_all/Scene1.png?raw=true)

### 4.2. Scene captured at 11/01/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230111/3_2_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjE4OTU3) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230111/3_6_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxMzc3)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing_all/Scene2.png?raw=true)

### 4.3. Scene captured at 15/01/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230115/1_0_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxMzgw) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230115/1_5_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxMzgy) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230115/8_2_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxMzg0)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing_all/Scene3.png?raw=true)

### 4.4. Scene captured at 30/03/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230330/0_6_imgsli.png?raw=true" width="250px" height = "300px">](https://imgsli.com/MjE4OTc2) 

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing_all/Scene4.png?raw=true)

### 4.5. Scene captured at 07/05/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230507/0_2_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxNDA1) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230507/1_0_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxNDI2) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230507/8_2_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxNDI4) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230507/8_6_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxNDI5)

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing_all/Scene5.png?raw=true)

### 4.6. Scene captured at 13/05/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230513/0_5_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxNDM0) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230513/15_2_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxNDQx) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230513/2_2_imgsli.png?raw=true" width="250px" height = "250px">](https://imgsli.com/MjIxNDM2) 

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing_all/Scene6.png?raw=true)

### 4.7. Scene captured at 13/07/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230713/3_0_imgsli.png?raw=true" width="250px" height = "200px">](https://imgsli.com/MjIxNTI0) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230713/3_1_imgsli.png?raw=true" width="250px" height = "200px">](https://imgsli.com/MjIxNDUz) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230713/6_0_imgsli.png?raw=true" width="250px" height = "200px">](https://imgsli.com/MjIxNTI5) 

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing_all/Scene7.png?raw=true)

### 4.8. Scene captured at 07/08/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230807/13_3_imgsli.png?raw=true" width="250px" height = "200px">](https://imgsli.com/MjIxNTQ3) 

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing_all/Scene8.png?raw=true)

### 4.9. Scene captured at 14/09/2023
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230914/1_1_imgsli.png?raw=true" width="150px" height = "250px">](https://imgsli.com/MjIxNTUw) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230914/14_3_imgsli.png?raw=true" width="150px" height = "250px">](https://imgsli.com/MjIxNTY5) 
[<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Automated_Processing_new/20230914/14_5_imgsli.png?raw=true" width="200px" height = "250px">](https://imgsli.com/MjE5MDE1) 

![image](https://github.com/RSingKK/Any-angle-MTF/blob/main/Time_Testing_all/Scene9.png?raw=true)

