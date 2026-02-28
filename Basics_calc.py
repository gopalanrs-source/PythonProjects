#basic calculator code to add 2 numbers
num1 = input("Enter the first number : ")
num2 = input("Enter the second number : ")
result = round(float(num1) + float(num2),2)
print(f"the sum of numbers is : {result:.2f}")