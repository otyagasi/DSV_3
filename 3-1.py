import pandas as pd
import matplotlib.pyplot as plt
FILE = "05k2022-1.xlsx"
df = pd.read_excel(FILE, skiprows=11, header=None)
age_count = list(df.iloc[2:52, 1]) + list(df.iloc[2:53, 10])
age = list(range(101))
plt.barh(age, age_count,color='green')
plt.show()
