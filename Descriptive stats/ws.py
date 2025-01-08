import matplotlib
import matplotlib.pyplot as plt
import plotly_express as px
import seaborn as sns
import math
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

file_path = 'C:/Users/junio/OneDrive/Documents/CESI/A3/Algo/Algo2/day.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Display the file
#print(df.to_string(index=False))
#print(df.info())
#print(df.describe().T)

pre_dropped = ["dteday", "casual", "registered", "instant"]
data_prep = df.drop(pre_dropped, axis=1)
data_prep.isnull().sum()
data_prep.hist(rwidth=0.9, figsize=(20, 20))
#plt.tight_layout()
#plt.show()
#correlation degree of all the numerical features wrt to the total count of bike.
data_prep[["temp", "atemp", "hum", "windspeed", "cnt"]].corr()["cnt"].plot(kind="bar", title="Correlation of variable features wrt to total number of bikes")

sns.boxplot(data=data_prep, x="cnt")

#data_prep.groupby("hr").mean()["cnt"].plot(kind="bar", figsize=(16, 8), color=cm(data_prep.groupby("hr").mean()["cnt"]/np.max(data_prep.groupby("hr").mean()["cnt"])))