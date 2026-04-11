import email

import pandas as pd

people = {
    "first" : ["Corey", "Jane", "John"],
    "last" : ["Schafer", "Doe", "Doe"],
    "email" : ["corey.schafer@gmail.com", "jane.doe@gmail.com", "john.smith@gmail.com"]
}

df = pd.DataFrame(people)
# print(df)

# for index, row in df.iterrows():
#     if row['last'] == 'Doe':
#         print(row['email'], row['first'], row['last'])

filt = (df['last'] == 'Doe') & (df['first'] == 'Jane')
print(df[-filt])
# print(df[-filt])  # - for negative filtering
# print(df[df['last'] == 'Doe']) # also possible
# print(df.loc[filt, 'email']) # also possible: print(df.loc[df['last'] == 'Doe', 'email'])


#update table/data
# df.columns = ['First Name', 'Last Name', 'Email']
# print(df)
# df.columns = [col.upper() for col in df.columns]
# print(df)
# df.columns = df.columns.str.replace(' ','_')
# print(df)
# df.rename(columns={'first':'First Name', 'last':'Last Name', 'email':'Email'}, inplace=True)
print(df)

# update rows
df.loc[2] = ['John', 'Smith', 'john.smith@email.com']
print(df)
df.loc[2, ['last', 'email']] = ['Doe', 'JohnDow@email.com']
print(df)
df.at[2, 'email'] = 'JohnDoe@email.com'
print(df)


print(df['email'].apply(lambda x: x.upper()))
print(df['email'].apply(len))


