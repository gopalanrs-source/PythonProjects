car = {"Model": "Hyundai", "Year" : 2020, "Price" : 650000, 
       "Model": "Tata Sierra", "Year" : 2026, "Price" : 1800000}
print(car)
print(len(car))

car2 = dict(Model = "Honda", Year = 2021, Price = 750000)
print(car2)

print(car["Model"])
print(car2["Price"])
print(car.get("Year"))
print(car.keys())
print(car.values())
print(car.items()) # returns a list of tuples containing key-value pairs

car["Model"] = "Maruti Suzuki"
print("-------------")
car.update({"Model": "Maruti Suzuki", "Year": 2022, "Price": 850000, "Color": "Red"})
print(car)
print(car.pop("Price"))
print(car)
car["EV"] = "yes"
print(car)
print(car.popitem())
car["EV"] = "yes"
print(car)
#del car["EV"]
print(car)
#car.clear()
print(car)
print("-------------")
car2 = car   # car2 = car creates a reference to the same dictionary object in memory, so changes to car2 will affect car and vice versa.
print(car2)
print(car)

car2["EV"] = "new"
print(car)


# good copy methods
car3 = car.copy()
car4 = dict(car)


