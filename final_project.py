# importing libraries
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import textwrap

# defining functions
def load_file(file_folder, filename):
    #determining filepath
    path = 'data/' + str(file_folder) + '/' + str(filename) + ".csv"

    #loading data into a matrix from CSV file, skipping first title row
    file = np.loadtxt(path, skiprows = 1, delimiter = ',', usecols = (1,2))

    #save vectors as their own variables
    right_eye = file[:, 0]
    left_eye = file[:, 1]

    return right_eye, left_eye

def statistical_test(signal_1, signal_2):
    # define alpha value
    alpha = 0.05

    # identify hypotheses
    # hypothesis H0: The Perg signal from signal_1 and signal_2 are statistically the same.
    # hypothesis H1: The Perg signal from signal_1 and signal_2 are statistically different.

    # conduct the t-test
    (stat, p_value) = ttest_ind(signal_1, signal_2, alternative = 'two-sided')

    # compare p_value and alpha
    if p_value < alpha:
        test_result = False #NOTE: False means reject H0, meaning signals are statistically different.
    else:
        test_result = True #NOTE: True means accept H0, meaning signals are statistically the same.

    return p_value, test_result

""" 
QUESTION 1: 
Is there a statistically significant difference between the right eye and left eye in healthy individuals in terms of PERG signal?
"""
# determining data location for loading the files into numpy arrays
file_folder_1 = "normal_no_notes"
normal_no_notes_file_list = ["0065", "0085", "0111", "0180", "0211", "0251", "0258", "0263", "0310", "0336"]
# creating empty lists to prevent overwriting data
nnn_right_eye_list = list()
nnn_left_eye_list = list()
# setting up for loop to iterate through the file list and load each file
for file in normal_no_notes_file_list:
    nnn_right_eye, nnn_left_eye = load_file(file_folder_1, file)
    nnn_right_eye_list.append(nnn_right_eye) # appending list to prevent variables being overwritten and lost
    nnn_left_eye_list.append(nnn_left_eye) # appending list to prevent variables being overwritten and lost

# separating each data set into a variable
subject_0065_r = nnn_right_eye_list[0]
subject_0085_r = nnn_right_eye_list[1]
subject_0111_r = nnn_right_eye_list[2]
subject_0180_r = nnn_right_eye_list[3]
subject_0211_r = nnn_right_eye_list[4]
subject_0251_r = nnn_right_eye_list[5]
subject_0258_r = nnn_right_eye_list[6]
subject_0263_r = nnn_right_eye_list[7]
subject_0310_r = nnn_right_eye_list[8]
subject_0336_r = nnn_right_eye_list[9]

subject_0065_l = nnn_left_eye_list[0]
subject_0085_l = nnn_left_eye_list[1]
subject_0111_l = nnn_left_eye_list[2]
subject_0180_l = nnn_left_eye_list[3]
subject_0211_l = nnn_left_eye_list[4]
subject_0251_l = nnn_left_eye_list[5]
subject_0258_l = nnn_left_eye_list[6]
subject_0263_l = nnn_left_eye_list[7]
subject_0310_l = nnn_left_eye_list[8]
subject_0336_l = nnn_left_eye_list[9]

# conducting statistical tests
nnn_p_value_1, nnn_test_result_1 = statistical_test(subject_0065_r, subject_0065_l)
nnn_p_value_2, nnn_test_result_2 = statistical_test(subject_0085_r, subject_0085_l)
nnn_p_value_3, nnn_test_result_3 = statistical_test(subject_0111_r, subject_0111_l)
nnn_p_value_4, nnn_test_result_4 = statistical_test(subject_0180_r, subject_0180_l)
nnn_p_value_5, nnn_test_result_5 = statistical_test(subject_0211_r, subject_0211_l)
nnn_p_value_6, nnn_test_result_6 = statistical_test(subject_0251_r, subject_0251_l)
nnn_p_value_7, nnn_test_result_7 = statistical_test(subject_0258_r, subject_0258_l)
nnn_p_value_8, nnn_test_result_8 = statistical_test(subject_0263_r, subject_0263_l)
nnn_p_value_9, nnn_test_result_9 = statistical_test(subject_0310_r, subject_0310_l)
nnn_p_value_10, nnn_test_result_10 = statistical_test(subject_0336_r, subject_0336_l)

# create a new list of test_results
nnn_test_result_list = list()
nnn_test_result_list.append(nnn_test_result_1)
nnn_test_result_list.append(nnn_test_result_2)
nnn_test_result_list.append(nnn_test_result_3)
nnn_test_result_list.append(nnn_test_result_4)
nnn_test_result_list.append(nnn_test_result_5)
nnn_test_result_list.append(nnn_test_result_6)
nnn_test_result_list.append(nnn_test_result_7)
nnn_test_result_list.append(nnn_test_result_8)
nnn_test_result_list.append(nnn_test_result_9)
nnn_test_result_list.append(nnn_test_result_10)

# count True and False results of the statistical tests
nnn_num_trues = nnn_test_result_list.count(True)
nnn_num_falses = nnn_test_result_list.count(False)

# print results
text_result_1 = textwrap.fill("Out of 10 statistical tests, " + str(
    nnn_num_trues) + " tests resulted in right and left eye data that was statistically the same and " + str(
    nnn_num_falses) + " tests resulted in right and left eye data that was statistically different.", width=175)
print(text_result_1)
if nnn_num_trues < nnn_num_falses:
    print("Based on these results, we can determine that right and left PERG data are statistically different.")
else:
    print("Based on these results, we can determine that right and left PERG data are statistically the same.")

# print space for separation between question answers
print(""
      "")

# plotting graphs for visual representations of data
# plot one signal to visualize data set
plt.plot(subject_0065_r)
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mv)")
plt.title("PERG Signal for Subject 0065")
plt.show()

# plot of all normal no notes right eye signals
plt.plot(subject_0065_r, label="Subject 0065")
plt.plot(subject_0085_r, label="Subject 0085")
plt.plot(subject_0111_r, label="Subject 0111")
plt.plot(subject_0180_r, label="Subject 0180")
plt.plot(subject_0211_r, label="Subject 0211")
plt.plot(subject_0251_r, label="Subject 0251")
plt.plot(subject_0258_r, label="Subject 0258")
plt.plot(subject_0263_r, label="Subject 0263")
plt.plot(subject_0310_r, label="Subject 0310")
plt.plot(subject_0336_r, label="Subject 0336")
plt.legend()
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("Right Eye PERG Signal for Normal Diagnoses with No Notes")
plt.show()

# plot of all normal no notes left eye signals
plt.plot(subject_0065_l, label="Subject 0065")
plt.plot(subject_0085_l, label="Subject 0085")
plt.plot(subject_0111_l, label="Subject 0111")
plt.plot(subject_0180_l, label="Subject 0180")
plt.plot(subject_0211_l, label="Subject 0211")
plt.plot(subject_0251_l, label="Subject 0251")
plt.plot(subject_0258_l, label="Subject 0258")
plt.plot(subject_0263_l, label="Subject 0263")
plt.plot(subject_0310_l, label="Subject 0310")
plt.plot(subject_0336_l, label="Subject 0336")
plt.legend()
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("Left Eye PERG Signal for Normal Diagnoses with No Notes")
plt.show()

# plot comparing right and left eye data of subject resulting in TRUE statistical test result (left and right are the same)
plt.plot(subject_0211_r, label="Right")
plt.plot(subject_0211_l, label="Left")
plt.legend()
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("Right and Left Eye Signal for Subject 0211")
plt.show()

# plot comparing right and left eye data of subject resulting in FALSE statistical test result (left and right are different)
plt.plot(subject_0065_r, label="Right")
plt.plot(subject_0065_l, label="Left")
plt.legend()
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("Right and Left Eye Signal for Subject 0065")
plt.show()

"""
QUESTION 2: 
Is there a statistically significant difference between the voltage output via PERG signal between healthy individuals and individuals with retintis pigmentosa?
"""
# determining data location for loading the files into numpy arrays
file_folder_2 = "retinitis_pigmentosa"
rp_file_list = ["0054", "0063", "0067", "0109", "0117", "0151", "0164", "0171", "0181", "0296"]
# create empty lists to prevent overwritten variables and lost data
rp_right_eye_list = list()
rp_left_eye_list = list()
# iterate through file list and load each file
for file in rp_file_list:
    rp_right_eye, rp_left_eye = load_file(file_folder_2, file)
    rp_right_eye_list.append(rp_right_eye)
    rp_left_eye_list.append(rp_left_eye)

# separate each data set into a variable
subject_0054_r = rp_right_eye_list[0]
subject_0063_r = rp_right_eye_list[1]
subject_0067_r = rp_right_eye_list[2]
subject_0109_r = rp_right_eye_list[3]
subject_0117_r = rp_right_eye_list[4]
subject_0151_r = rp_right_eye_list[5]
subject_0164_r = rp_right_eye_list[6]
subject_0171_r = rp_right_eye_list[7]
subject_0181_r = rp_right_eye_list[8]
subject_0296_r = rp_right_eye_list[9]

subject_0054_l = rp_left_eye_list[0]
subject_0063_l = rp_left_eye_list[1]
subject_0067_l = rp_left_eye_list[2]
subject_0109_l = rp_left_eye_list[3]
subject_0117_l = rp_left_eye_list[4]
subject_0151_l = rp_left_eye_list[5]
subject_0164_l = rp_left_eye_list[6]
subject_0171_l = rp_left_eye_list[7]
subject_0181_l = rp_left_eye_list[8]
subject_0296_l = rp_left_eye_list[9]

# conduct statistical tests
# comparing right eye data of RP patients to Normal Diagnoses patients
rp_p_value_1_r, rp_test_result_1_r = statistical_test(subject_0054_r, subject_0065_r)
rp_p_value_2_r, rp_test_result_2_r = statistical_test(subject_0063_r, subject_0085_r)
rp_p_value_3_r, rp_test_result_3_r = statistical_test(subject_0067_r, subject_0111_r)
rp_p_value_4_r, rp_test_result_4_r = statistical_test(subject_0109_r, subject_0180_r)
rp_p_value_5_r, rp_test_result_5_r = statistical_test(subject_0117_r, subject_0211_r)
rp_p_value_6_r, rp_test_result_6_r = statistical_test(subject_0151_r, subject_0251_r)
rp_p_value_7_r, rp_test_result_7_r = statistical_test(subject_0164_r, subject_0258_r)
rp_p_value_8_r, rp_test_result_8_r = statistical_test(subject_0171_r, subject_0263_r)
rp_p_value_9_r, rp_test_result_9_r = statistical_test(subject_0181_r, subject_0310_r)
rp_p_value_10_r, rp_test_result_10_r = statistical_test(subject_0296_r, subject_0336_r)

# comparing right eye data of RP patients to Normal Diagnoses patients
rp_p_value_1_l, rp_test_result_1_l = statistical_test(subject_0054_l, subject_0065_l)
rp_p_value_2_l, rp_test_result_2_l = statistical_test(subject_0063_l, subject_0085_l)
rp_p_value_3_l, rp_test_result_3_l = statistical_test(subject_0067_l, subject_0111_l)
rp_p_value_4_l, rp_test_result_4_l = statistical_test(subject_0109_l, subject_0180_l)
rp_p_value_5_l, rp_test_result_5_l = statistical_test(subject_0117_l, subject_0211_l)
rp_p_value_6_l, rp_test_result_6_l = statistical_test(subject_0151_l, subject_0251_l)
rp_p_value_7_l, rp_test_result_7_l = statistical_test(subject_0164_l, subject_0258_l)
rp_p_value_8_l, rp_test_result_8_l = statistical_test(subject_0171_l, subject_0263_l)
rp_p_value_9_l, rp_test_result_9_l = statistical_test(subject_0181_l, subject_0310_l)
rp_p_value_10_l, rp_test_result_10_l = statistical_test(subject_0296_l, subject_0336_l)

# create a new list of test results
rp_test_result_list = list()
rp_test_result_list.append(rp_test_result_1_r)
rp_test_result_list.append(rp_test_result_2_r)
rp_test_result_list.append(rp_test_result_3_r)
rp_test_result_list.append(rp_test_result_4_r)
rp_test_result_list.append(rp_test_result_5_r)
rp_test_result_list.append(rp_test_result_6_r)
rp_test_result_list.append(rp_test_result_7_r)
rp_test_result_list.append(rp_test_result_8_r)
rp_test_result_list.append(rp_test_result_9_r)
rp_test_result_list.append(rp_test_result_10_r)
rp_test_result_list.append(rp_test_result_1_l)
rp_test_result_list.append(rp_test_result_2_l)
rp_test_result_list.append(rp_test_result_3_l)
rp_test_result_list.append(rp_test_result_4_l)
rp_test_result_list.append(rp_test_result_5_l)
rp_test_result_list.append(rp_test_result_6_l)
rp_test_result_list.append(rp_test_result_7_l)
rp_test_result_list.append(rp_test_result_8_l)
rp_test_result_list.append(rp_test_result_9_l)
rp_test_result_list.append(rp_test_result_10_l)

# count True and False test results of the statistical tests
rp_num_trues = rp_test_result_list.count(True)
rp_num_falses = rp_test_result_list.count(False)

# print results
text_result_2 = textwrap.fill("Out of 20 statistical tests, " + str(rp_num_trues) +
      " tests resulted in RP and normally diagnosed PERG data that was statistically the same and " + str(rp_num_falses) +
      " tests resulted in RP and normally diagnosed PERG data that was statistically different.", width=175)
print(text_result_2)
if rp_num_trues < rp_num_falses:
    print("Based on these results, we can determine that PERG data from normally diagnosed individuals and individuals diagnosed with retinitis pigmentosa are statistically different.")
else:
    print("Based on these results, we can determine that PERG data from normally diagnosed individuals and individuals diagnosed with retinitis pigmentosa are statistically the same.")

# print space to separate question answers
print(""
      "")

# plotting results
# plotting right eye retinitis pigmentosa data
plt.plot(subject_0054_r, label="Subject 0054")
plt.plot(subject_0063_r, label="Subject 0063")
plt.plot(subject_0067_r, label="Subject 0067")
plt.plot(subject_0109_r, label="Subject 0109")
plt.plot(subject_0117_r, label="Subject 0117")
plt.plot(subject_0151_r, label="Subject 0151")
plt.plot(subject_0164_r, label="Subject 0164")
plt.plot(subject_0171_r, label="Subject 0171")
plt.plot(subject_0181_r, label="Subject 0181")
plt.plot(subject_0296_r, label="Subject 0296")
plt.legend()
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("Right Eye PERG Signal for Retinitis Pigmentosa Condition")
plt.show()

# plotting left eye retinitis pigmentosa data
plt.plot(subject_0054_l, label="Subject 0054")
plt.plot(subject_0063_l, label="Subject 0063")
plt.plot(subject_0067_l, label="Subject 0067")
plt.plot(subject_0109_l, label="Subject 0109")
plt.plot(subject_0117_l, label="Subject 0117")
plt.plot(subject_0151_l, label="Subject 0151")
plt.plot(subject_0164_l, label="Subject 0164")
plt.plot(subject_0171_l, label="Subject 0171")
plt.plot(subject_0181_l, label="Subject 0181")
plt.plot(subject_0296_l, label="Subject 0296")
plt.legend()
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("Left Eye PERG Signal for Retinitis Pigmentosa Condition")
plt.show()

# plot of TRUE statistical test result
plt.plot(subject_0171_r, label="Subject 0171 (Retinitis Pigmentosa)")
plt.plot(subject_0263_r, label="Subject 0263 (Normal)")
plt.legend()
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("PERG Signal for Statistically Same Data")
plt.show()

# plot of FALSE statistical test result
plt.plot(subject_0054_l, label="Subject 0054 (Retinitis Pigmentosa)")
plt.plot(subject_0065_l, label="Subject 0065 (Normal)")
plt.legend()
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("PERG Signal for Statistically Different Data")
plt.show()

"""
QUESTION 3: 
Is there a statistically significant difference between the voltage output via PERG signal between healthy individuals with and without mercury poisoning?
"""
# determining data location for loading files into numpy arrays
file_folder_3 = "normal_mercury_poisoning"
nmp_file_list = ["0035", "0124", "0212", "0218", "0225", "0266", "0272", "0274", "0281", "0329"]
# create empty lists to prevent overwritten variables and lost data
nmp_right_eye_list = list()
nmp_left_eye_list = list()
# iterate through file list and load each file
for file in nmp_file_list:
    nmp_right_eye, nmp_left_eye = load_file(file_folder_3, file)
    nmp_right_eye_list.append(nmp_right_eye)
    nmp_left_eye_list.append(nmp_left_eye)

# separate each data set into a variable
subject_0035_r = nmp_right_eye_list[0]
subject_0124_r = nmp_right_eye_list[1]
subject_0212_r = nmp_right_eye_list[2]
subject_0218_r = nmp_right_eye_list[3]
subject_0225_r = nmp_right_eye_list[4]
subject_0266_r = nmp_right_eye_list[5]
subject_0272_r = nmp_right_eye_list[6]
subject_0274_r = nmp_right_eye_list[7]
subject_0281_r = nmp_right_eye_list[8]
subject_0329_r = nmp_right_eye_list[9]

subject_0035_l = nmp_left_eye_list[0]
subject_0124_l = nmp_left_eye_list[1]
subject_0212_l = nmp_left_eye_list[2]
subject_0218_l = nmp_left_eye_list[3]
subject_0225_l = nmp_left_eye_list[4]
subject_0266_l = nmp_left_eye_list[5]
subject_0272_l = nmp_left_eye_list[6]
subject_0274_l = nmp_left_eye_list[7]
subject_0281_l = nmp_left_eye_list[8]
subject_0329_l = nmp_left_eye_list[9]

# conduct statistical tests
# comparing right eye data of normal diagnoses vs. normal diagnoses with mercury poisoning
nmp_p_value_1_r, nmp_test_result_1_r = statistical_test(subject_0035_r, subject_0065_r)
nmp_p_value_2_r, nmp_test_result_2_r = statistical_test(subject_0124_r, subject_0085_r)
nmp_p_value_3_r, nmp_test_result_3_r = statistical_test(subject_0212_r, subject_0111_r)
nmp_p_value_4_r, nmp_test_result_4_r = statistical_test(subject_0218_r, subject_0180_r)
nmp_p_value_5_r, nmp_test_result_5_r = statistical_test(subject_0225_r, subject_0211_r)
nmp_p_value_6_r, nmp_test_result_6_r = statistical_test(subject_0266_r, subject_0251_r)
nmp_p_value_7_r, nmp_test_result_7_r = statistical_test(subject_0272_r, subject_0258_r)
nmp_p_value_8_r, nmp_test_result_8_r = statistical_test(subject_0274_r, subject_0263_r)
nmp_p_value_9_r, nmp_test_result_9_r = statistical_test(subject_0281_r, subject_0310_r)
nmp_p_value_10_r, nmp_test_result_10_r = statistical_test(subject_0329_r, subject_0336_r)

# comparing left eye data of normal diagnoses vs. normal diagnoses with mercury poisoning
nmp_p_value_1_l, nmp_test_result_1_l = statistical_test(subject_0035_l, subject_0065_l)
nmp_p_value_2_l, nmp_test_result_2_l = statistical_test(subject_0124_l, subject_0085_l)
nmp_p_value_3_l, nmp_test_result_3_l = statistical_test(subject_0212_l, subject_0111_l)
nmp_p_value_4_l, nmp_test_result_4_l = statistical_test(subject_0218_l, subject_0180_l)
nmp_p_value_5_l, nmp_test_result_5_l = statistical_test(subject_0225_l, subject_0211_l)
nmp_p_value_6_l, nmp_test_result_6_l = statistical_test(subject_0266_l, subject_0251_l)
nmp_p_value_7_l, nmp_test_result_7_l = statistical_test(subject_0272_l, subject_0258_l)
nmp_p_value_8_l, nmp_test_result_8_l = statistical_test(subject_0274_l, subject_0263_l)
nmp_p_value_9_l, nmp_test_result_9_l = statistical_test(subject_0281_l, subject_0310_l)
nmp_p_value_10_l, nmp_test_result_10_l = statistical_test(subject_0329_l, subject_0336_l)

# create a new list of test results
nmp_test_result_list = list()
nmp_test_result_list.append(nmp_test_result_1_r)
nmp_test_result_list.append(nmp_test_result_2_r)
nmp_test_result_list.append(nmp_test_result_3_r)
nmp_test_result_list.append(nmp_test_result_4_r)
nmp_test_result_list.append(nmp_test_result_5_r)
nmp_test_result_list.append(nmp_test_result_6_r)
nmp_test_result_list.append(nmp_test_result_7_r)
nmp_test_result_list.append(nmp_test_result_8_r)
nmp_test_result_list.append(nmp_test_result_9_r)
nmp_test_result_list.append(nmp_test_result_10_r)
nmp_test_result_list.append(nmp_test_result_1_l)
nmp_test_result_list.append(nmp_test_result_2_l)
nmp_test_result_list.append(nmp_test_result_3_l)
nmp_test_result_list.append(nmp_test_result_4_l)
nmp_test_result_list.append(nmp_test_result_5_l)
nmp_test_result_list.append(nmp_test_result_6_l)
nmp_test_result_list.append(nmp_test_result_7_l)
nmp_test_result_list.append(nmp_test_result_8_l)
nmp_test_result_list.append(nmp_test_result_9_l)
nmp_test_result_list.append(nmp_test_result_10_l)

# count True and False test results of the statistical tests
nmp_num_trues = nmp_test_result_list.count(True)
nmp_num_falses = nmp_test_result_list.count(False)

# print results
text_result_3 = textwrap.fill("Out of 20 statistical tests, " + str(rp_num_trues) +
      " tests resulted in normally diagnosed with and without mercury poisoning PERG data that was statistically the same and " + str(rp_num_falses) +
      " tests resulted in normally diagnosed with and without mercury poisoning PERG data that was statistically different.", width = 175)
print(text_result_3)
if rp_num_trues < rp_num_falses:
    print("Based on these results, we can determine that PERG data from normally diagnosed individuals and individuals with mercurcy poisoning are statistically different.")
else:
    print("Based on these results, we can determine that PERG data from normally diagnosed individuals and individuals with mercury poisoning are statistically the same.")


# plotting
# plotting right eye mercury poisoning for each subject
plt.plot(subject_0035_r, label="Subject 0035")
plt.plot(subject_0124_r, label="Subject 0124")
plt.plot(subject_0212_r, label="Subject 0212")
plt.plot(subject_0218_r, label="Subject 0218")
plt.plot(subject_0225_r, label="Subject 0225")
plt.plot(subject_0266_r, label="Subject 0266")
plt.plot(subject_0272_r, label="Subject 0272")
plt.plot(subject_0274_r, label="Subject 0274")
plt.plot(subject_0281_r, label="Subject 0281")
plt.plot(subject_0329_r, label="Subject 0329")
plt.legend()
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("Right Eye PERG Signal for Mercury Poisoning Condition")
plt.show()

# plotting left eye mercury poisoning for each subject
plt.plot(subject_0035_l, label="Subject 0035")
plt.plot(subject_0124_l, label="Subject 0124")
plt.plot(subject_0212_l, label="Subject 0212")
plt.plot(subject_0218_l, label="Subject 0218")
plt.plot(subject_0225_l, label="Subject 0225")
plt.plot(subject_0266_l, label="Subject 0266")
plt.plot(subject_0272_l, label="Subject 0272")
plt.plot(subject_0274_l, label="Subject 0274")
plt.plot(subject_0281_l, label="Subject 0281")
plt.plot(subject_0329_l, label="Subject 0329")
plt.legend()
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("Left Eye PERG Signal for Mercury Poisoning Condition")
plt.show()

# plot of TRUE statistical test result
plt.plot(subject_0272_l, label="Mercury Poisoning")
plt.plot(subject_0258_l, label="Normal No Notes")
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("PERG Signal for Statistically Same Data")
plt.legend()
plt.show()

#plot of FALSE statistical tes result
plt.plot(subject_0035_r, label="Mercury Poisoning")
plt.plot(subject_0065_r, label="Normal No Notes")
plt.xlabel("Data Point")
plt.ylabel("PERG Signal (mV)")
plt.title("PERG Signal for Statistically Different Data")
plt.legend()
plt.show()
