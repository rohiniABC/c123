import csv
import statistics
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv("savings_data.csv")
quant_saved=df['quant_saved'].tolist()
highschool=df['highschool_completed'].tolist()
quantSaved=[]
highSchool=[]
for i in  range(0,len(highschool)-1):
  if (highschool[i]!=0):
    highSchool.append(highschool[i])
    quantSaved.append(quant_saved,highschool_completed[i])

correlation=np.corrcoef(quantSaved,)
print(correlation)