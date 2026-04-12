import email

import pandas as pd

people = {
    "first" : ["Corey", "Jane", "John","Adam"],
    "last" : ["Schafer", "Doe", "Doe", "Doe"],
    "email" : ["corey.schafer@gmail.com", "jane.doe@gmail.com", "john.smith@gmail.com","adam.doe@gmail.com"]
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
#print(df)
df.loc[2, ['last', 'email']] = ['Doe', 'JohnDow@email.com']
#print(df)
df.at[2, 'email'] = 'JohnDoe@email.com'
#print(df)


#print(df['email'].apply(lambda x: x.upper()))
#print(df['email'].apply(len))

df['full_name'] = df['first'] + ' ' + df['last']
# print(df)
df.drop(columns=['first','last'], inplace=True)
# print(df)
df[['first','last']] = df['full_name'].str.split(' ', expand=True)
# print(df)

print(df)                   
df.loc[len(df)] = {'email': 'tony.stark@email.com','full_name': 'Tony Stark','first': 'Tony', 'last': 'Stark'}
print(df)                   
new_row = pd.DataFrame([{'first': 'Banner'}]) 
df = pd.concat([df, new_row], ignore_index=True)
print(df)


people2 = {
    "first" : ["Black", "Captain"],
    "last" : ["Widow", "America"],
    "email" : ["black.widow@gmail.com", "captain.america@gmail.com"]
}

df2 = pd.DataFrame(people2)
print(df2)
df = pd.concat([df, df2], ignore_index=True)
# df.drop(index=4, inplace=True)
# print(df)
# filt = (df['last'] == 'Doe') 
# df.drop(index=df[filt].index, inplace=True)
df.sort_values(by=['last', 'first'], ascending=[False, True], inplace=True)
print(df)
df.sort_index(inplace=True)
print(df)
