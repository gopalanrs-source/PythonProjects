age = int(input("Enter Student age : "))

if age_val >= 14 and age_val <= 18:
    print("Studen is in High School")
elif age_val > 18 and age_val <=22:
     print("Student is in college")   
elif age_val <14 and age_val >= 5:
     print("Student is in middle school")
elif age_val < 5:
     print("Student is in elementary school")
else :
     print("Student is out of school")   

print(age_val if age_val <= 18 else "Student is out of school")
print("ternary operation in python" if age_val > 1 else "else condition of ternary operation")


      

