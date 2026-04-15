import pandas as pd

numbers = pd.Series([1,2,3,4,5])
# print("Q1---------------------")
# print(numbers)


sales = pd.Series(
    [100,200,300],
    index=['a','b','c']
    )
# print("Q2---------------------")
# print(sales)

people = pd.DataFrame(
    {"Name":["Ravi","Anita"],
     "Age" : [28,32]
     }
)
# print("Q3---------------------")
# print(people)

cities = pd.DataFrame({
    "City": ["Chennai","Mumbai"],
    "Population":[8,20]
}, index=["row1","row2"])
# print("Q4---------------------")
# print(cities)

reviews = pd.read_csv("farm_data.csv")
people.to_csv("people.csv", index=False)
people["Salary"] = [50000,60000]
# print("Q5---------------------")
# print(people)

print(people["Salary"].dtype)

data = {
    "country": ["India", "USA", "France", "India", "USA"],
    "price": [10, 25, 15, 20, 30],
    "points": [90, 85, 88, 92, 87]
}

reviews = pd.DataFrame(data)
print("Lesson 2 - Q1 ---------------------")
print(reviews)

countries = reviews["country"]
print(countries)
print("Lesson 2 - Q2 ---------------------")
first_row = reviews.iloc[0]
print(first_row)

price_value = reviews.loc[1, "price"]
print("Lesson 2 - Q3 ---------------------")
print(price_value)

expensive = reviews[reviews["price"] > 20]
print("Lesson 2 - Q4 ---------------------")
print(expensive)


subset = reviews[["country", "price"]]
print("Lesson 2 - Q5 ---------------------")
subset["avg"] = reviews["price"]/reviews["points"]
print(subset)

filt = reviews["country"] == "India"
indian_wines = reviews[filt]
print("Lesson 2 - Q6 ---------------------")
print(indian_wines)



first_three = reviews.iloc[0:3]
first_three = reviews.iloc[0:3]["price"]
print("Lesson 2 - Q7 ---------------------")
print(first_three)

reviews["discounted_price"] = reviews["price"] - 5
print("Lesson 2 - Q8 ---------------------")
print(reviews)

sample_reviews = reviews.loc[[1,3]]
print("Lesson 2 - Q9 ---------------------")
print(sample_reviews)

# df = reviews.loc[0:100,["country","price"]]



print("Lesson 2 - Q10 ---------------------")
print(df)



