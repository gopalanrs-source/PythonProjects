import pandas as pd

data = pd.read_csv("data/students.csv")
print(data.head())

data["Average"] = data[["Math","Science","English"]].mean(axis=1)
print(data.head())
print(data[["Name","Average"]])

top_scorer = data.loc[data["Average"].idxmax()]
# print("\nTop Scorer result:")
# print(top_scorer)
print("\nTop Scorer:")
print(top_scorer["Name"], "-", round(top_scorer["Average"], 2))

low_scorer = data.loc[data["Average"].idxmin()]
# print("\nLowp Scorer result:")
# print(low_scorer)
print("\nLowp Scorer:")
print(low_scorer["Name"], "-", round(low_scorer["Average"],2))

data["Result"] = data["Average"].apply(lambda x: "Pass" if x >= 60 else "Fail")
print("\nFinal Report:")
print(data[["Name", "Average", "Result"]])

passed = (data["Result"] == "Pass").sum()
class_avg = data["Average"].mean()

def grader(row):
    if row['Average'] >= 90:
        return "A"
    elif row['Average'] >= 75:
        return "B"
    elif row['Average'] >= 60:
        return "C"
    else :
        return "F"

data["Grade"] = data.apply(grader, axis=1)
print(data.head(5))

fail = data[data["Result"] == "Fail"]
print(fail)
