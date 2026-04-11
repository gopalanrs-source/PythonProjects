import pandas as pd

df = pd.read_csv('data/survey_results_public.csv', index_col ='Respondent')
scheme_df = pd.read_csv('data/survey_results_schema.csv', index_col ='Column')

# print(df.head())
# print(scheme_df.head())

Countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']

Sal_filter = (df['ConvertedComp'] > 100000) & (df['Country'].isin(Countries)) & (df['LanguageWorkedWith'].str.contains('HTML'))
print(df.loc[Sal_filter, ['Country','EdLevel','LanguageWorkedWith','ConvertedComp']])
# print(df[Sal_filter], 'Respondent', 'EdLevel','ConvertedComp')

df.rename(columns={'ConvertedComp':'SalaryUSD'}, inplace=True)
df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})




                         

