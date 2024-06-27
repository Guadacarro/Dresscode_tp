import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('prendas.csv')
pd.set_option('display.max_rows', len(df))

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='talle' ,color='magenta')
plt.xlabel('Talle')
plt.ylabel('Cantidad')
plt.title('Cantidad de Prendas por Talle')
plt.show()