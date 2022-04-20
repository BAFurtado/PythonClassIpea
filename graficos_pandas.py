import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ts = pd.Series(np.random.randn(10000), index=pd.date_range("1/1/2020", periods=10000))
ts.tail()
ts = ts.cumsum()
ts.tail()
ts.plot()
plt.show()
# Try with 10,000

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2020", periods=1000))
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()
#
fig, ax = plt.subplots()
# https://matplotlib.org/stable/gallery/color/named_colors.html
df.plot(ax=ax, color=['black', 'grey', 'yellowgreen', 'teal'])
ax.legend(frameon=False)
plt.show()
#
# # Other kinds given by kind=''
# # ‘bar’ or ‘barh’ for bar plots
# # ‘hist’ for histogram
# # ‘box’ for boxplot
# # ‘kde’ or ‘density’ for density plots
# # ‘scatter’ for scatter plots
#
# # https://matplotlib.org/stable/gallery/color/named_colors.html
df.iloc[0].plot(kind='bar')
plt.show()
# #
df.head().reset_index()[['A', 'B', 'C']].plot(kind='bar')
plt.show()
# #
df.A.plot(kind='hist', bins=20)
plt.show()
# #
df.B.plot(kind='box')
plt.show()
# #
df.plot(kind='kde')
plt.show()
# #
fig, ax = plt.subplots()
df.plot(x='A', y='B', kind='scatter', color='blue', marker='.', alpha=.5, ax=ax)
df.plot(x='C', y='D', kind='scatter', color='red', marker='+', alpha=.5, ax=ax)
ax.set(xlabel='Trendy AC', ylabel='BD', title='Crazy nonsense pleonastic')
plt.savefig('meu_pandas_plot.png', format='png', dpi=350)
plt.show()
