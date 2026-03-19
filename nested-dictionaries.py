model1 = {"Name": "XUV700", "Brand": "Mahindra", "Price": 1500000}
model2 = {"Name": "Tata Sierra", "Brand": "Tata", "Price": 1800000}
car = {"Model1": model1, "Model2": model2}
print(car)
print(car["Model1"]["Name"])
print(str(car["Model2"]["Price"])+car["Model2"]["Name"])
