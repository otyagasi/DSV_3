import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data2.csv')
plt.plot(df.iloc[:, 0], df.iloc[:, 1],linewidth=0.5, c='blue')
plt.ylim(-20, 50)
plt.show()