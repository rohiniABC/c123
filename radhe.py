import pandas as pd
import plotly.express as pe
df=pd.read_csv("savings_data.csv")
fig=pe.scatter(df,y="quant_saved",color="highschool_completed")
fig.show()