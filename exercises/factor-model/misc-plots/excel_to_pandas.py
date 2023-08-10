import pandas as pd
df = pd.read_csv('2023-07-20_11-00-06_positivity_report_batch.csv',
                   usecols=[0, 2, 8, 9], skiprows=[0])
df.columns = ['ID', 'dataset', 'biomarker', 'counts']
print(df)


df_pivoted = df.pivot(index='ID', columns='biomarker', 
                      values='counts')

print(df_pivoted.shape)
print(df_pivoted.loc[:,'single positive CD81-CF647'].mean())
