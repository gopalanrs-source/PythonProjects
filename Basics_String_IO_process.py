print("Basic String and IO operation in Python")
first_name = input("Enter your first name : ")
last_name = input("Enter your Last name : ")
year_dob = input("Enter year of DOB : ")
patient_type = input("Enter patient type New/Old : ")
current_year = 2026


print("Name : "+first_name+ " "+last_name)
print("Patient type : "+patient_type)
print("Age : "+ str(current_year - int(year_dob)))
      