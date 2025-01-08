import matplotlib
import matplotlib.pyplot as plt
import plotly_express as px
import seaborn as sns
import math
import numpy as np
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

file_path = r'C:\Users\junio\OneDrive\Documents\CESI\A3\Algo\Algo2\n.xlsx'

try:
    df = pd.read_excel(file_path)
    print(df.head())  # Display the first few rows
except PermissionError as e:
    print(f"Permission Error: {e}")
except FileNotFoundError as e:
    print(f"File Not Found Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Display the file
#print(df.to_string(index=False))
#print(df.info())
#print(df.describe().T)

x= df['x'];
y= df['coffee'];
corr = np.corrcoef(x,y);
print(corr[0,1])