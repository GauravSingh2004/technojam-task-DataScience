import numpy as np
import pandas as pd
df = pd.read_csv("obesity_data.csv")
df.head()
print(df.iloc[0, :].unique())
df.drop([0,1,2], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
df.drop(df.columns[1::3], axis=1, inplace=True)
df.head()
for i in range(1,85):
    df.iloc[:,i] = df.iloc[:,i].str.split(expand=True)[0]
df.head()
df2 = df.melt(id_vars=['Unnamed: 0'], value_name='obesity_rate')
df2.head()
df2[['year','gender']] = df2.iloc[:,1].str.split('.', expand=True)
df2.head()
df2.drop('variable', axis=1, inplace=True)
gender = {'1':'male', '2':'female'}
df2.gender.replace(gender, inplace=True)
df2.rename(columns={'Unnamed: 0':'country'}, inplace=True)
df2.head()
df2.shape
(16380, 4)
df2.isna().sum()
df2.dtypes
df2[df2.obesity_rate == 'No']['country'].unique()
omit = df2[df2.obesity_rate == 'No']['country'].unique()
df2[df2.country.isin(omit)]['obesity_rate'].unique()
df2 = df2[~df2.country.isin(omit)]
df2 = df2.astype({'obesity_rate': 'float32'})
df2.dtypes


