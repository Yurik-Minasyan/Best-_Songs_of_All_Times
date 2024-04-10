import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv("/content/drive/MyDrive/Colab Notebooks/song_data.csv")
print("-------------------HEAD-------------------")
df.head()
print("-------------------INFO-------------------")
df.info()
print("-------------------SHAPE-------------------")
df.shape
print("-------------------DESCRIPTION-------------------")
df.describe()
print("-------------------CORR(?)-------------------")
df.corr()
print("-------------------HEAT_MAP-------------------")
plt.subplots(figsize=(20,15))
sns.heatmap(df.corr(),annot=True,cmap="YlGnBu")
print("-------------------HISTOGRAM-------------------")
df.hist(figsize=(20,20))
print("-------------------PLOTS(?)-------------------")
sns.pairplot(df, )
t1 = df.loc[(df['song_popularity'] == 100)]
t1['song_name'].unique()
t2 = df.loc[(df['song_popularity'] > 95)]
t2['song_name'].unique()
#graphigs N1
fig, ax = plt.subplots()
ax.bar(df['song_popularity'], df['song_duration_ms'],color = "tab:blue")

ax.set_ylabel('Duration')
ax.set_title("Song popularity by it's duration")

plt.show()
#graphigs N2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv("/content/drive/MyDrive/Colab Notebooks/song_data.csv")

fig, ax = plt.subplots()
ax.bar(df['song_popularity'], df['loudness'],color = "tab:blue")

ax.set_ylabel('Loudness')
ax.set_title("Song loudness by it's popularity")

plt.show()
