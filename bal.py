import csv
import statistics
import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv("savings_data.csv")
data=df["quant_saved"].tolist()
fig=ff.create_distplot([data],["saving"],show_hist=False)
fig.show()