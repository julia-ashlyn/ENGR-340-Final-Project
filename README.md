# ENGR-340-Final-Project
This project is Julia Larson's Final Project for ENGR 340 at JMU. This project focuses on comparing PERG-IOBA Datasets from patients with various diagnoses to determine if there is a difference between PERG signal results from subjects with various diagnosis conditions. 

**General Topic**

The conditions included in this program are (1) a diagnosis of "Normal" with no additional notes, (2) a diagnosis of "Retinitis Pigmentosa" with no additional notes or secondary diagnoses, and (3) a diagnosis of "Normal" with additional notes of "Mercury Poisoning". 
The purpose of this program is to use statistical analysis and graphical comparison of PERG signals at various conditions to determine if the pattern electroretinogram could aid in diagnosing retinitis pigmentosa. To do this, three questions of interest are posed: 

(1) Is there a difference in PERG signal trends and values between the right and left eye in individual "Normal No Notes" Condition? 

(2) Are PERG signal trends and values different between individuals with retinitis pigmentosa and normal diagnoses? 

(3) Is there a difference between PERG signals of subjects with normal and mercury poisoning diagnoses? 

**Depedencies and Additional Programs**

This program requires that the following packages be installed: 

scipy

numpy

matplotlib

textwrap

**Main Programs**

The main program of this repository is final_project.py. It is the only program required to run the program to analyze the data. Functions are defined within the main program. 

**Tutorial**

To operate this code, you must simply have all of the data downloaded and ensure the pathways remain the same as set up in the repository. Then, you run the main code, final_project.py. 
Initially, there are two functions defined. One to load the file and return the right eye and left eye PERG signals, load_file(). The second to conduct a two-sided t-test, statistical_test(), returning the p_value and the result of the test in the form of True, meaning the signals are statistically the same, or False, the signals are statistically different. The code then moves on to answering the questions in order. 

**Sample of Results**

Results of statistical tests: 
![image](https://github.com/user-attachments/assets/5dc0153b-064b-46fb-beeb-18b7b2ba1095)


**Limitations of Program**

This program is only able to analyze the data files included in the repository. Although the program functions as it should and does compare signals from various conditions, the tests may not be the best method to determine if the pattern electroretinogram could be used to aid in diagnostic practices for retinitis pigmentosa. This is because comparing the right eye of normal with no note conditions against each other resulted also in a statistically different result. Therefore, no PERG signal seems to really be statistically similar enough to warrant meaninful conclusions solely based on the statistical analysis. 

The above observations reveal that it is important to observe the graphical visualizations of the data and compare shapes of the graphs when determining differences between PERG signals of 

**Future Results** 

In the future, this program could develop into being able to compare more data files. In the current code, there are only 30 data files being compared, 10 for each condition. Ideally, the program would be iterated to be able to include more data files. 

Additionally, this code could be iterated after a better understanding of PERG data is grasped and how results are used in a clinical setting. 
