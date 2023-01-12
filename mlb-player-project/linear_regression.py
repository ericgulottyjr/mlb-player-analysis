import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

#create a "scaled" dataset which will be used in regression
scaler.fit(final21[["RC", "WAR", "Salary"]])
scaled21 = pd.DataFrame()
scaled21[["RC", "WAR", "Salary"]] = scaler.transform(final21[["RC", "WAR", "Salary"]])

#basic stats to predict runs created
y1 = total21["RC"]
X1 = total21[basic]
A_basic = np.column_stack([np.ones(len(X1), dtype = 'int'), X1])
b_h_basic = np.linalg.inv(A_basic.T @ A_basic) @ A_basic.T @ y1

#basic stats to predict WAR
y2 = final21["WAR"]
X2 = final21[basic]
A_basic2 = np.column_stack([np.ones(len(X2), dtype = 'int'), X2])
b_h_basic2 = np.linalg.inv(A_basic2.T @ A_basic2) @ A_basic2.T @ y2

#salary to predict runs created
y3 = scaled21["Salary"]
X3 = scaled21["WAR"]
A_salary = np.column_stack([np.ones(len(X3), dtype = 'int'), X3])
b_h_salary = np.linalg.inv(A_salary.T @ A_salary) @ A_salary.T @ y3

#scaled salary to predict WAR
y4 = scaled21["WAR"]
X4 = scaled21["Salary"]
A_salary1 = np.column_stack([np.ones(len(X4), dtype = 'int'), X4])
b_h_salary1 = np.linalg.inv(A_salary1.T @ A_salary1) @ A_salary1.T @ y4