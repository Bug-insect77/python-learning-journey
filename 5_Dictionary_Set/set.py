#set is a collection of non-repetitive elements 
my_set={1,2,3,4,5,6}
my_set2={1,2,3,7,8,9}
# s.add(1)
# s.add(3)
# my_set.union(my_set2)
# new_set = my_set.intersection(my_set2)
# print(new_set)


print(my_set)
# add()	Adds a single element to the set
# update()	Adds multiple elements (from iterable like list, set, tuple, etc.) to the set

my_set.add(55)
print(my_set)
my_set.update([22,33,44],{12,21,11})
print(my_set)