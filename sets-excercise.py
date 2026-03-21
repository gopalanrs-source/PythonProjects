#sets

num = {1,2,3,4,5}
num2 = set((1,2,3,4))

print(num)
print(num2)
print(type(num))
print(type(num2))

nums = {1,True, 2,False,3,0,4,5,5,5}
print(nums)
#sets are unordered, unindexed, and do not allow duplicate values. They are mutable, but the elements contained in a set must be immutable.
print(2 in nums)
print(6 in nums)
# you cannot access items in a set by referring to an index or a key, but you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

nums.add(9)
morenums = (6,7,6,6,6,8) 
print("              ")
print(morenums)
nums.update(morenums)# the duplicates inside morenums will be removed
print(nums)


one = {1,2,3,4,5}
two = {4,5,6,7,8}

newset = one.union(two) # shows all the elements from both sets, but removes any duplicates
print(newset)

one.intersection_update(two) # shows the common elements between the two sets
print(one)

one.symmetric_difference_update(two) # shows the elements that are not common between the two sets
print(one)

