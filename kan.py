import seaborn as sns
import pandas as pd
df=pd.read_csv("savings_data.csv")
sns.boxplot(data=df,x=df["quant_saved"])
q1=df["quant_saved"].quantile(0.25)
q3=df["quant_saved"].quantile(0.75)
iqr=q3-q1
print("q1 is",q1)
print("q3 is",q3)
lower=q1-(1.5*iqr)
upper=q3+(1.5*iqr)
print("lowerWhiscker is", lower)
print("upperWhisker is", upper)
newdf=df[df["quant_saved"]<upper]
print(newdf["quant_saved"])