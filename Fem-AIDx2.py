#import packages
import pandas as pd
import numpy as np
import statistics
import scipy.stats as stats

#import data files, will be one data file per question
#used a randomly generated data set for code testing purposes :)
#Q1: Have you ever felt dismissed by a Health Care Professional whilst seeking diagnosis? (scale of 1-10, 1= never, 5= sometimes, 10= frequently)
#scaling of response and question itself do not reflect final format

Q1 = pd.read_csv(r"C:\Users\kvwl626\OneDrive - AZCollaboration\Documents\Q1.csv")
Q1 = Q1.rename(columns={'rank': 'score', 'F/M': 'Gender'})
print(Q1)

#set split conditions
print("")
Male = "M"

Q1_M = Q1[Q1['Gender'] == Male]
print (Q1_M)

print("")

#split dataframe into M and F scores
List_Q1_M = Q1_M['Rank'].tolist()
print('List from column Rank:')
print(List_Q1_M)

Q1_M_Sum = sum(List_Q1_M)
Q1_M_Mean = statistics.mean(List_Q1_M)

print("")

print("")
Female = "F"
Q1_F = Q1[Q1['Gender'] == Female]
print (Q1_F)

List_Q1_F = Q1_F['Rank'].tolist()
print('List from column Rank:')
print(List_Q1_F)

Q1_F_Sum = sum(List_Q1_F)
Q1_F_Mean = statistics.mean(List_Q1_F)
print("")

#statistically summaries
print("Q1 Statsistical Summary for Males")
print("Mean = " ,Q1_M_Mean)
print("Total Score = " ,Q1_M_Sum)

print("")
print("Q1 Statsistical Summary for Females")
print("Mean = " ,Q1_F_Mean)
print("Total Score = " ,Q1_F_Sum)


#T-test for significance 
print("")
print("T-Test Results for Q1")
Q1_F_array = np.array(List_Q1_F)
Q1_M_array = np.array(List_Q1_M)

t_statistic, p_value = stats.ttest_ind(Q1_F_array, Q1_M_array)

alpha = 0.05
df = len(Q1_F_array)+len(Q1_M_array)-2
critical_t = stats.t.ppf(1 - alpha/2, df)

print("")
print("T-value:", t_statistic)
print("P-Value:", p_value)
print("Critical t-value:", critical_t)

print("")
print('With T-value')
if np.abs(t_statistic) >critical_t:
    print('There is significant difference between two groups')
else:
    print('No significant difference found between two groups')
 
print("")
print('With P-value')
if p_value >alpha:
    print('No evidence to reject the null hypothesis that a significant difference between the two groups')
else:
    print('Evidence found to reject the null hypothesis that a significant difference between the two groups')
    
#What the scores indicate of patients experience, scaling will be randomised for each question, 
#e.g. 10 may mean a negative experience on one question, and positive on another 
print("")
if Q1_F_Sum > Q1_M_Sum:
    print("Scores for females were higher, indicating a negative experience for Q1")
if Q1_M_Sum > Q1_F_Sum:
    print("Scores for males were higher, indicating a negative experience for Q1")
if Q1_M_Sum == Q1_F_Sum:
    print("Score were equal for both genders")


#redofor Q2, Q3 etc.. 
#collate all statistical summaries into a pdf file report
