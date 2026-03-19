my_num_tuple = (1,3,4,5,6)
my_text_tuple = tuple(('John', 24,"seattle"))
mytext2 = tuple(("joe","doe","jane"))


print(my_num_tuple)
print(my_text_tuple)
print(mytext2)

newlist = list(mytext2)
newlist.append("smith")
newtuple = tuple(newlist)
print(newtuple)


#unpacking tuples
my_tuple = ("apple", "banana", "cherry","mango","grape")
(green, yellow, *red)= my_tuple

print(green)
print(yellow)
print(red)

(one,*two) = red
print(one)
print(two)
print(my_tuple.count("apple"))



