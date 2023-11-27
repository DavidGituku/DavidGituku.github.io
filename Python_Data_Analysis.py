import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("Data_Analysis.xlsx")
print(df.head())
Q1_2021= (df.iloc[0:63]) #filtering for the first quarter year 2021
print(np.var(Q1_2021))# obtaining the variances for the columns
Vol_Q1_2021=(math.sqrt(Q1_2021['Day to Day diffrence'].var(ddof=0))*0.5)# obtaining the volatility for Day to day diference columns
print(Vol_Q1_2021)
Q2_2021=(df.iloc[63:124])
print(np.var(Q2_2021))
Vol_Q2_2021=(math.sqrt(Q2_2021['Day to Day diffrence'].var(ddof=0))*0.5)
print(Vol_Q2_2021)
Q3_2021=(df.iloc[124:189]) 
print(np.var(Q3_2021))
Vol_Q3_2021=(math.sqrt(Q3_2021['Day to Day diffrence'].var(ddof=0))*0.5)
print(Vol_Q3_2021)
Q4_2021=(df.iloc[189:251]) 
print(np.var(Q4_2021))
Vol_Q4_2021=(math.sqrt(Q4_2021['Day to Day diffrence'].var(ddof=0))*0.5)
print(Vol_Q4_2021)
Q1_2022=(df.iloc[251:315])
print(np.var(Q1_2022))
Vol_Q1_2022=(math.sqrt(Q1_2022['Day to Day diffrence'].var(ddof=0))*0.5)
print(Vol_Q1_2022)
Q2_2022=(df.iloc[315:375])
print(np.var(Q2_2022))
Vol_Q2_2022=(math.sqrt(Q2_2022['Day to Day diffrence'].var(ddof=0))*0.5)
print(Vol_Q2_2022)
Q3_2022=(df.iloc[375:438])
print(np.var(Q3_2022))
Vol_Q3_2022=(math.sqrt(Q3_2022['Day to Day diffrence'].var(ddof=0))*0.5)
print(Vol_Q3_2022)
Q4_2022=(df.iloc[438:500])
print(np.var(Q4_2022))
Vol_Q4_2022=(math.sqrt((Q4_2022['Day to Day diffrence'].var(ddof=0)))*0.5)
print(Vol_Q4_2022) 
X=['Q1','Q2','Q3','Q4']
Y=[Vol_Q1_2021,Vol_Q2_2021,Vol_Q3_2021,Vol_Q4_2021]
W=['Q1','Q2','Q3','Q4']
Z=[Vol_Q1_2022,Vol_Q2_2022,Vol_Q3_2022,Vol_Q4_2022]
plt.plot(X, Y,label="Line 1")
plt.plot(W, Z,label="Line 2")
plt.title("Volatility movement for years 2021&2022 ")
