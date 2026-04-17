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

# print(people["Salary"].dtype)

data = {
    "country": ["India", "USA", "France", "India", "USA"],
    "price": [10, 25, 15, 20, 30],
    "points": [90, 85, 88, 92, 87]
}

reviews = pd.DataFrame(data)
# print("Lesson 2 - Q1 ---------------------")
# print(reviews)

countries = reviews["country"]
# print(countries)
# print("Lesson 2 - Q2 ---------------------")
first_row = reviews.iloc[0]
# print(first_row)

price_value = reviews.loc[1, "price"]
# print("Lesson 2 - Q3 ---------------------")
# print(price_value)

expensive = reviews[reviews["price"] > 20]
# print("Lesson 2 - Q4 ---------------------")
# print(expensive)


subset = reviews[["country", "price"]]
# print("Lesson 2 - Q5 ---------------------")
subset["avg"] = reviews["price"]/reviews["points"]
# print(subset)

filt = reviews["country"] == "India"
indian_wines = reviews[filt]
# print("Lesson 2 - Q6 ---------------------")
# print(indian_wines)



first_three = reviews.iloc[0:3]
first_three = reviews.iloc[0:3]["price"]
# print("Lesson 2 - Q7 ---------------------")
# print(first_three)

reviews["discounted_price"] = reviews["price"] - 5
# print("Lesson 2 - Q8 ---------------------")
# print(reviews)

sample_reviews = reviews.loc[[1,3]]
# print("Lesson 2 - Q9 ---------------------")
# print(sample_reviews)

# df = reviews.loc[0:100,["country","price"]]



# print("Lesson 2 - Q10 ---------------------")
# print(df)


data = {
    "country": ["India", "USA", "France", "India", "USA"],
    "price": [10, 25, 15, 20, 30],
    "points": [90, 85, 88, 92, 87]
}

reviews = pd.DataFrame(data)
# print("Lesson 3 - Q1 ---------------------")
# print(reviews)
# print(reviews["price"].mean())

max_points = reviews["points"].max()
# price_summary = reviews["price"].agg(["min", "max", "mean"])
price_summary = reviews["price"].describe()
# print("Lesson 3 -------")
# print(price_summary)

counrty_counts = reviews["country"].value_counts()

new_prices = reviews["price"].map(lambda p: p+5)
# print("Lesson 3 - Q4 ---------------------")
# print(new_prices)
reviews["double_points"] = reviews["points"].apply(lambda p: p*2)
# print("Lesson 3 - Q5 ---------------------")        
# print(reviews)

# data = {
#     "country": ["India", "USA", "France", "India", "USA", "France"],
#     "price": [10, 25, 15, 20, 30, 18],
#     "points": [90, 85, 88, 92, 87, 91],
#     "variety": ["A", "B", "A", "C", "B", "A"]
# }
# reviews = pd.DataFrame(data)


# average_price = reviews.groupby("country")["price"].mean()
# sorted_reviews = reviews.sort_values(by="price")
# sorted_reviews = reviews.sort_values(by="price",ascending=False)
# counrty_counts = reviews["country"].value_counts()
# max_points = reviews.groupby("country")["points"].max().sort_values(ascending=False)
# print(max_points)
# multi_sort = reviews.sort_values(by=["country","price"], ascending=[True,False])
# group_two = reviews.groupby(["country","variety"])["price"].mean()
# highest_price = reviews.groupby(["country","variety"])["price"].max().sort_values(ascending=False)
# print(highest_price)

reviews = pd.read_csv("data/mini_wine_reviews.csv")

# print(reviews.head())

bargain_wine = reviews.loc[(reviews.points / reviews.price).idxmax(), 'title']
#  reviews.loc[condition's idxmax(), 'title']
#  reviews.loc[3, 'title'] 
# print(bargain_wine)
# print(reviews.loc[reviews.price.idxmax(), 'title'])
# print(reviews.loc[reviews.points.idxmax(), 'title'])

tropical_count = reviews.description.map(lambda desc: 'tropical' in desc).sum()
fruity_count = reviews.description.map(lambda desc: 'fruity' in desc).sum()
print(f"tropical_count ",{tropical_count})
print(f"fruity_count ",{fruity_count})
print(tropical_count)
print(fruity_count)
desc_counts = pd.Series([tropical_count, fruity_count], index = ['tropical','fruity'])
print(desc_counts)

def stars(row):
    if row['country'] == 'Cananda' or row['points'] >= 95:
        return 3
    elif row['points'] >= 85:
        return 2
    else:
        return 1
    
star_ratings = reviews.apply(stars, axis=1)
print(star_ratings)

taster_twitter_handle = reviews.taster_twitter_handle.value_counts()
taster_twitter_handle = reviews.groupby('taster_twitter_handle').size()
print(taster_twitter_handle)




