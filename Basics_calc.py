#basic calculator code to add 2 numbers
num1 = input("Enter the first number : ")
num2 = input("Enter the second number : ")
result = round(float(num1) + float(num2),2)
#use round for calculating the result upto 2 decimal places
#use f-string for printing the result with 2 decimal places
print(f"the sum of numbers is : {result:.2f}")
print(f"the sum of numbers is : {result:.3f}")
#test commit2
