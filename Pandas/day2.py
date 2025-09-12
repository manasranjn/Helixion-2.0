import pandas as pd

# dFrame1 = pd.read_csv("business-operations-survey-2022-business-finance.csv", encoding="cp1252")
# dFrame2 = pd.read_excel("file_example.xls")
dFrame3 = pd.read_json("titanic-parquet.json", lines=True)
# print(dFrame3.head())
# print(dFrame3.tail(10))
# print(dFrame3.shape)
# print(dFrame3.info())
# print(dFrame3.describe())
# print(dFrame3.columns)
# print(dFrame3.dtypes)

#Column
col1 = dFrame3['Name']
# print(col1)
col2 = dFrame3[['Survived', 'Name', 'Age']]
# print(col2)
dFrame3['newCol'] = dFrame3['Name']
# print(dFrame3['newCol'])
# dFrame3.drop(['Name'], axis=1, inplace=True)
# dFrame3.drop(['newCol'], axis=1, inplace=True)
# print(dFrame3)

#Rows
# print(dFrame3.iloc[50])
# print(dFrame3.loc[dFrame3['Survived'] == 1])
# print(dFrame3)

# print(dFrame3.head())
#
# dFrame3.drop(2, inplace=True)
# print(dFrame3.head())

data = {"Name": ["Manas", "Rudra"], "Age": [25, 22], "Marks": [20, 20]}
dFrame3 = pd.DataFrame.from_dict(data)
df = pd.DataFrame(data)

df.loc[len(df)] = ["Sumit", 23, 25]
# print(df)

sum = df['Age'] + df['Marks']
# print(sum)

multi = df['Age'] * df['Marks']
# print(multi)

# Conditional Selection
# print(df['Age']>22)
# data2 = df[(df['Age']>22) & (df['Marks']> 20)]
# print(data2)

name = df['Name'] == "Manas"
# print(name)

df["newCol"] = df["Name"] == "Rudra"
# print(df)