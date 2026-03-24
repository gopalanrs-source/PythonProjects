person = "Gopal"
sal = 1000000

player = {"name": "Virat Kohli", "age": 34, "team": "India", "runs": 12000}

# Use f-string to print the following sentence:

print(f"{person} has a salary of {sal} per month")
print(f"{person}'s annual salary is {sal*12}")
print(f"{person.capitalize()} - salary = {sal:.2f}")
print(f"{player['name']} is {player['age']} years old and plays for {player['team']}.")

for num in range(1,11):
    print(f"{num} X 2.25 / 1.618 = {(num * 2.25)/1.618:%}") 
    # print(f"{num} X 2.25 = {num * 2.25:.3f}")