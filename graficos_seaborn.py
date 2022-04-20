import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Source: https://medium.com/@bernardolago/gr%C3%A1ficos-usando-seaborn-61f7d23481cf
# Alternativamente, use o endereço
bit = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1618758590&period2=1650294590&interval=1d&events=history&includeAdjustedClose=true')

df_bitcoin = pd.read_csv('https://datahub.io/cryptocurrency/bitcoin/r/bitcoin.csv')
df_bitcoin = df_bitcoin.tail(50)

plt.figure(figsize=(8, 6))
plt.xticks(rotation=90, fontsize=4)
sns.set_theme(style="darkgrid")

# LINEPLOT
# sns.lineplot(data=df_bitcoin, x='date', y='price(USD)', color='red')
sns.lineplot(data=bit, x='Date', y='Close', color='red')
plt.show()

titanic = sns.load_dataset("titanic")
df_por_sexo = titanic.groupby('sex')['survived'].sum().reset_index()

plt.figure(figsize=(8, 6))
# BARPLOT
sns.barplot(data=df_por_sexo, x='sex', y='survived')
plt.show()

# BOXPLOT
sns.boxplot(data=titanic, x='age')
plt.show()

# HISTPLOT
sns.histplot(data=titanic, x='age')
plt.show()

voos = sns.load_dataset("flights")
# Pivot. Organize: INDEX, COLUMNS, VALUES
voos_pivoted = voos.pivot("month", "year", "passengers")

plt.figure(figsize=(10, 6))
# HEATMAP
# Notice the easy formatting
sns.heatmap(voos_pivoted, annot=True, fmt='.0f')
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
# HEATMAP
# Notice the easy formatting
# Check alternative colormap 'cmap' parameters:
# https://matplotlib.org/stable/gallery/color/colormap_reference.html
sns.heatmap(voos_pivoted, annot=True, fmt='.0f', ax=ax, cmap='coolwarm')
ax.set(xlabel='Trendy x_label', ylabel='Meses em inglês', title='Desnecessário título')
plt.tight_layout()
plt.show()
