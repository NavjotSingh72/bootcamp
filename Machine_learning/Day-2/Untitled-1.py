# %%


# %%
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd

df = pd.read_csv("dataset.csv")
print(df.head())
df = pd.read_csv(r"C:\Users\Navjot\Downloads\dataset.csv")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("dataset.csv")

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %%
spotify = pd.read_csv("/kaggle/input/-spotify-tracks-dataset/dataset.csv").head(100)
spotify

# %% [markdown]
# # In my spotify dataset. I wanted to see if the tempo affected how long a song is. As you can see below,there is a slight correlation between a songs tempo and duration.

# %%
sums_lmplot = sns.lmplot(x="tempo", y="duration_ms", data=spotify)

# %% [markdown]
# # Next, I wanted see how dance-able songs are compared to there popularity rating. In the plot below, it seems as though the higher the acoustic songs popularity is, the dance-able is around .6.

# %%
spotify_plot = sns.relplot(x="danceability",y="popularity", data=spotify.head(30), hue="track_genre")
spotify_plot.set_xticklabels(rotation=90)



