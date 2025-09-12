import pandas as pd
import numpy as np

# print(pd.__version__)

#Series
# sr1 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
# print(sr1)
# print(sr1['c'])
# print(sr1[3])

#DatFrame
# dFrame1 = pd.DataFrame({"First":[1,2,3],"Second":[4,5,6]})
# print(dFrame1)

# dFrame2 = pd.DataFrame([[1,2,3],[4,5,6]])
# print(dFrame2)

# npArr = np.array([[1,2,3],[4,5,6]])
# dFrame3 = pd.DataFrame(npArr, columns=["A", "B", "C"])
# print(dFrame3)

dFrame4 = pd.read_csv("business-operations-survey-2022-business-finance.csv", encoding="cp1252")
# dFrame5 = pd.read_excel("file_example.xls")
dFrame6 = pd.read_json("titanic-parquet.json", lines=True)
print(dFrame6.head())

# print(dFrame6)