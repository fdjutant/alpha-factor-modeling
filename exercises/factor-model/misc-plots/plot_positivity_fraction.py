import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing

## import the csv file
filename = 'Chip1-PS_positivity_report_batch.csv'

# convert the csv file into pandas dataframe
df = pd.read_csv(filename, usecols=[0, 2, 8, 9])
df.columns = ['ID', 'dataset', 'biomarker', 'counts']
# print(df)

# pivot the data
df_pivoted = df.pivot_table(index='ID', columns='biomarker', 
                      values='counts', sort=False)
# print(df_pivoted)

# call specific biomarker counts
# print(df_pivoted.loc[:,'CD63'].mean())
# print(df_pivoted.iloc[:,1:].mean().shape)
# print(df_pivoted.columns[:-1])

## plot the positivity results
# compute mean and sem
data = df_pivoted.iloc[:,:-1].mean()
errors = df_pivoted.iloc[:,:-1].sem()
data_percentage = data/data.sum() * 100
x = range(len(data))
labels = ['CD63', 'CD81', 'CD9', 'CD63,\n CD81',
          'CD63,\n CD9', 'CD81,\n CD9',
          'CD63,\n CD81, CD9']

# plot the data using a bar plot
plt.style.use("dark_background")    # compatible with black background
font_size=14
fig, ax = plt.subplots(figsize=(10, 7))
ax2 = ax.twinx()
ax.bar(x, data, yerr=errors, 
       capsize=5, width=0.5,
       color='#1f77b4', ecolor='white',
       edgecolor='white', linewidth=1.2)
ax2.bar(x, data_percentage, capsize=0, width=0)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=font_size)
ax.set_xlabel('Biomarker(s)', fontsize=font_size)
ax.set_ylabel('Number of clusters', fontsize=font_size)
ax2.set_ylabel('Biomarker fraction (%)', fontsize=font_size)
ax.set_title(filename + '\n', fontsize=font_size)
ax.set_ylim([None, 200])

# create a separation line between single, double, and triple
for i in range(3, len(data), 3):
    ax.axvline(i - 0.5, color='white', linestyle='--')

# remove top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# show and save plot as png
plt.savefig(filename[:-4]+'-test-plot.png', transparent=True)
plt.show()