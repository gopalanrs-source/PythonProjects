grocery_list = ["milk","eggs","bread", "butter"]
print(grocery_list)
print(grocery_list[-1])
print(grocery_list[0:3])


grocery_list.append("cookies")
grocery_list.extend(["Chocolates", "Ice Cream"])
grocery_list += ["Chips", "Soda"]
print(grocery_list)
grocery_list.insert(2,"bananas")
print(grocery_list)
grocery_list.remove("bread")
print(grocery_list)
grocery_list.pop()
print(grocery_list)
grocery_list[2:2] = ["grapes","oranges"] # inserts "grapes" and "oranges" at index 2 without replacing any existing items
print(grocery_list)
grocery_list[1:3] = ["sugarcane","papaya"]  # replaces the items at index 1 and 2 with "sugarcane" and "papaya"
print(grocery_list)
