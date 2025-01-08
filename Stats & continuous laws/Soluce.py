import matplotlib
import matplotlib.pyplot as plt
import plotly_express as px
import seaborn as sns
import numpy as np
import math
import pandas as pd
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

file_path = 'C:/Users/junio/OneDrive/Documents/CESI/A3/Algo/Algo3/server_usage_data.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Display the file
#print(df.to_string(index=False))
#print(df.info())
#print(df.describe().T)

#data_prep = df.head()
#data_prep.isnull().sum()
#data_prep.hist(rwidth=0.9, figsize=(20, 20))
#plt.tight_layout()
#plt.show()

x= df['CPU_Usage'];
y= df['Temperature'];
corr = np.corrcoef(y,x);
#print(corr[0,1])

a= df['Memory_Usage'];
b= df['Temperature'];
corr = np.corrcoef(a,b);
#print(corr[0,1])

c= df['Network_Usage'];
d= df['Temperature'];
corr = np.corrcoef(c,d);
#print(corr[0,1])

corr = np.corrcoef(x,a);
#print(corr[0,1]) => 0.42966209604263134

corr = np.corrcoef(x,a);
#print(corr[0,1])

c = df['Network_Usage'].values.reshape(-1, 1)  # Reshaping required for sklearn
d = df['Temperature'].values

# Step 1: Create a linear regression model and fit the data
model = LinearRegression()
model.fit(c, d)

# Step 2: Predict values based on the model
d_pred = model.predict(c)

# Step 3: Get the slope (coefficient) and intercept of the line
slope = model.coef_[0]
intercept = model.intercept_

# Step 4: Plot the data points and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(c, d, color='blue', label='Data points')  # Plot data points
plt.plot(c, d_pred, color='red', label=f'Regression line: y = {slope:.2f}x + {intercept:.2f}')  # Plot regression line
plt.xlabel('Network Usage')
plt.ylabel('Temperature')
plt.title('Linear Regression of Network Usage vs Temperature')
plt.legend()

# Display the plot
plt.show()

# Optional: Print the correlation coefficient and regression equation
corr = np.corrcoef(df['Network_Usage'], df['Temperature'])[0, 1]
print(f"Correlation Coefficient: {corr}")
print(f"Regression Equation: y = {slope:.2f}x + {intercept:.2f}")

data = df['Temperature']

# Step 3: Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

# Step 4: Calculate the IQR
IQR = Q3 - Q1

# Step 5: Define lower and upper bounds for anomalies
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Step 6: Find anomalies (values outside the IQR range)
anomalies = data[(data < lower_bound) | (data > upper_bound)]

# Print results
#print(f'Q1 (25th percentile): {Q1}')
#print(f'Q3 (75th percentile): {Q3}')
#print(f'IQR: {IQR}')
#print(f'Lower bound: {lower_bound}')
#print(f'Upper bound: {upper_bound}')
#print(f'Number of anomalies: {len(anomalies)}')

# Optionally print the anomalies themselves
#print('Anomalies:')
#print(anomalies)

