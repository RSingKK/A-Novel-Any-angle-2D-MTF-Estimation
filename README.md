# A Novel Any-angle 2D MTF Estimation for Single Satellite Image Super-Resolution
## 1. Python Supported

1. Step one: Automaticly extract edge-objects with any-angle. Automatic_Any_Angle_Roi_Selection.py
2. Step Two: Calculate 1D MTF of each edge-object with any-angle. Calculate_1D_MTF.py
3. Step Three: Use two demisional Gaussian function to estimate 2D MTF. Fit_Gaussian_2D_MTF.py
4. Step Four: Perform SSIR on single satellite scene image. Image_MTF_SSIR.py
5. Step Five: SSIR_Assessment.py


## 2. More Comparison Results
More qualitative and quantitative comparison results on public datasets (Ucmerced dataset, WHU-RS19 dataset, and RSSCN7 dataset) are shown as follows. / denotes that the result has been distorted.


<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20picture/parkinglot_compare.png?raw=true" width="300px">
[![parkinglot](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20picture/parkinglot_compare.png?raw=true)](https://imgsli.com/MjE1NzI2)

<img src="https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20picture/airport_compare.png?raw=true" width="300px">
[![airport](https://github.com/RSingKK/Any-angle-MTF/blob/main/Some%20uploaded%20picture/airport_compare.png?raw=true)](https://imgsli.com/MjE1NzM0)



### 1. UCMerced Dataset

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/30fce002-b4fd-4568-a8c5-f24686ad996d)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/e656e732-79cd-4fb2-80f2-005719126700)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/d14c1654-306d-49d1-9bba-4161478b9563)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/6d0bb861-8232-45fb-beba-4d15ba624319)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/6075e6ab-4a18-4568-a98f-5219c61b65ca)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/f6ace178-f4a3-42e4-a1ba-caed8ab41da6)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/aca245d8-4cb5-4095-946b-b9a7dd0953fd)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/7f3f91e8-74f4-4069-b769-5c247dd462a3)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/bf18e81b-776d-4f5c-9520-a3a04f82312a)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/e9cd0041-10f8-4126-a287-1fa17ce6a885)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/43dec535-55d7-479d-91da-01ced586d41c)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/576f1365-7e72-4473-8ad6-cd0ec9db9fcd)

### 2. WHU-RS19 Dataset

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/60ad4122-b1cf-45e7-939a-7a27bdd12bf8)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/aca8b69d-c5d3-484f-a0f8-ad1f99594032)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/7a53183a-41a0-41d5-a58c-bcc5bf20cddc)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/0cee8a11-b196-4c62-a121-01af647bf53e)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/d5e79d27-311c-4ad3-b87a-1dad511104e3)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/6d76df4e-cd1e-4ddb-9a42-9b16282b757b)

### 3. RSSCN7 Dataset

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/231edc0b-2ac6-47c1-a3cc-3a4ede7498a8)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/cb3e8afe-a30d-4959-afb0-d880107ebd8f)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/6e7b2385-7d89-4031-b007-b6a422b2bb97)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/d5874fe1-77ed-4bfd-b65c-8a5accdb0fd4)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/e754d050-aa93-449d-88f1-0c7865b5bea1)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/af9d043a-4b3a-4d22-a656-2d3a162c1b2e)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/19adf9b2-d44b-4de9-b671-a00be653c0bd)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/8b3b3672-a6c8-4aaa-9129-21ab4700fe1c)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/9ab60e02-ad36-4805-8355-a41feceeada7)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/0f15fcfc-afc3-48e0-93fe-36e32a81ac9c)

![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/ef233974-0a4c-42a5-b9f8-d6d245031680)
![image](https://github.com/RSingKK/A-Novel-Any-angle-2D-MTF-Estimation/assets/49096921/896dc45e-008b-4d17-9f04-af7f3fdef504)



