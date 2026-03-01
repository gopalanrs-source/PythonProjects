course = "Python for Beginners"
print(course.find("for"))
print("Python" in course)
course2 = course.replace("for", "4")
course3 = course.replace("Beginners","Everyone")
print(course)
print(course2)
print(course3)
course = course2+course3
print(course)
#string is immutable in python. We cannot change the string but we can create a new string by concatenating the old string with the new string.

