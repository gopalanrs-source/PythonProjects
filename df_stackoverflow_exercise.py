import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

na_vals = ['NA', 'Missing']
df = pd.read_csv('data/survey_results_public.csv', index_col ='Respondent', na_values=na_vals)
scheme_df = pd.read_csv('data/survey_results_schema.csv', index_col ='Column')

# print(df.head())
# print(scheme_df.head())

Countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']

Sal_filter = (df['ConvertedComp'] > 100000) & (df['Country'].isin(Countries)) & (df['LanguageWorkedWith'].str.contains('HTML'))
# print(df.loc[Sal_filter, ['Country','EdLevel','LanguageWorkedWith','ConvertedComp']])
# print(df[Sal_filter], 'Respondent', 'EdLevel','ConvertedComp')

df.rename(columns={'ConvertedComp':'SalaryUSD'}, inplace=True)
df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})

df.sort_values(by=['Country', 'SalaryUSD'], ascending=[True, False], inplace=True)
# print(df[['Country','SalaryUSD']].head(50))
# print(df['SalaryUSD'].nlargest(10))
# print(df.nlargest(10, 'SalaryUSD')[['Country','SalaryUSD', 'EdLevel', 'Employment']])
# print(df.nsmallest(10, 'SalaryUSD')[['Country','SalaryUSD']])
# print(df['SalaryUSD'].median())
#print(df.median())
# print(df.describe())
# print(df['Hobbyist'].value_counts())
# print(df['SocialMedia'].value_counts(normalize=True))

country_grp = df.groupby('Country')
# print(country_grp['SalaryUSD'].median().sort_values(ascending=False))
# print(country_grp.get_group('United States'))

# filt2 = df['Country'] == 'India'
# print(df.loc[filt2]['SocialMedia'].value_counts())

# print(country_grp['SocialMedia'].value_counts().head(50))
# print(country_grp['SocialMedia'].value_counts().loc['India'])

# print(country_grp['SalaryUSD'].agg(['median', 'mean', 'min', 'max', 'count']))

# print(country_grp['SalaryUSD'].median().loc['India'])

filt = df['Country'] == "India"
# print(df.loc[filt]['LanguageWorkedWith'].str.contains('Python').value_counts())
# print(df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum())   # sum will not work on groupby object, it will work on series object. So we need to filter the dataframe first and then apply the sum function on the series object.

python_users = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
country_respondents = df['Country'].value_counts()
# python_pct = (python_users / country_respondents) * 100
# print(python_pct.sort_values(ascending=False))

python_df = pd.concat([country_respondents, python_users], axis='columns', sort=False)
# print(python_df.head(5))
python_df.columns = ['TotalRespondents', 'PythonUsers'] 
python_df['PythonPct'] = (python_df['PythonUsers'] / python_df['TotalRespondents']) * 100
# print(python_df.sort_values(by='PythonPct', ascending=False).head(10))
# print(python_df.loc['India'])
print(df['YearsCode'].value_counts())
print(df['YearsCode'].unique())
print(df['YearsCode'].nunique())
df['YearsCode'] = df['YearsCode'].replace('Less than 1 year', 0)
df['YearsCode'] = df['YearsCode'].replace('More than 50 years', 51)
print(df['YearsCode'].unique())
df['YearsCode'] = df['YearsCode'].astype('float')
print(df['YearsCode'].mean())












      

      


                         

