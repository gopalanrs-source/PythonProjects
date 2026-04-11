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



