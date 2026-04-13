import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('data/survey_results_public.csv', index_col ='Respondent')
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
print(df.median())

      


                         

