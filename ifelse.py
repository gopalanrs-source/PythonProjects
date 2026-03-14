age = int(input("Enter Student age : "))

if age >= 14 and age <= 18:
    print("Studen is in High School")
elif age > 18 and age <=22:
     print("Student is in college")   
elif age <14 and age >= 5:
     print("Student is in middle school")
elif age < 5:
     print("Student is in elementary school")
else :
     print("Student is out of school")   

print(age if age <= 18 else "Student is out of school")
print("ternary operation in python" if age > 1 else "else condition of ternary operation")


      

