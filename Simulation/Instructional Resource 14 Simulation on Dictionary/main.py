# Python Simulation 14
# Sets in Python

#working with set
print()
even_nums = {2,4,6,8,10}
emp_data = {1, "Junell", 5.5, True, 1.1}    #True and 1 are treated the same
num = {1,2,3,2,1,4,5,5,4,6,7}
raw_num = {(10,10), 20, 30}
m = {False, True, 0}

print(f"Set of Even Numbers: {even_nums}")
print(f"Employee Data: {emp_data}")
print(f"Numbers: {num}")
print(f"Raw Number: {raw_num}")
print(f"Boolean: {m}")

#create a set
print()
s = set()
print(s, type(s), sep=" --> ", end="\n\n")

#transforming into set
print()
s1 = set("Hello")
print(s1)
s2 = set((1,2,3,4,5))
print(s2)
my_dict = {1:"One", 2:"Two", 3:"Three"}
s3 = set(my_dict)
print(s3)

#modifying a set
print()
set1 = set()
print(set1)
set1.add(10)
print(set1)
set1.add(20)
set1.add(30)
print(set1)
raw_num = {21, 13,5, 7, 9}
print(raw_num)
set1.update(raw_num)
print(f"New Set of Numbers: {set1}")

#set union
print()
s1 = {1,2,3,4,5}; s2 = {4,5,6,7,8,9}
print(s1, s2, s1|s2, s1.union(s2), s2.union(s1), sep="\n")

#set intersection
print()
print(s1, s2, sep="\n")
print(s1&s2)
print(s1.intersection(s2), s2.intersection(s1), sep="\n")

#set difference
print()
print(s1, s2, sep="\n")
print(s1-s2)

#set symmetric difference
print()
print(s1, s2, sep="\n")
print(s1^s2)

#adding set elements
print()
prog_lang = {"Python", "c++", "Java", "PHP"}
print(prog_lang)
prog_lang.add("Go")
prog_lang.add("Dart")
print()
print(f"List of Programming Languages: {prog_lang}")

#clearing a set
print()
prog_lang.clear()
print(f"Cleared Set: {prog_lang}")

#copying a set element
print()
g1 = {"Matthew", "John", "Mark"}
print(g1)
g2 = g1.copy()
print(g2)
g2.add("Luke")
print(f"G1 = {g1}")
print(f"G2 = {g2}")

#popping set element
print()
agencies = {"DICT", "DSWD", "DENR", "DPWH", "DOH"}
print(f"Government Agencies: {agencies}")
print(agencies.pop(), agencies, sep="\n")
#agencies.pop(2)    #set.pop() takes no arguments
#print(f"Updated Agencies: {agencies}")

#removing set element
print()
cities = {"Surigao", "Butuan", "Bislig", "Bayugan", "Cabadbaran", "Tandag"}
print(f"Cities in Caraga: {cities}")
cities.remove("Surigao")
print(cities, "\n")

#working with list to set and back to a list
print()
odd_num_list = [1,3,5,7,9,3,5,1,7,11,15,17,15,21,5]
print("List of Odd Numbers:", odd_num_list)
print("List of Unique Odd Numbers:", list(set(odd_num_list)))

#set of sets with frozenset
"""
frozensets are often used in situations where you need to ensure 
that the set of elements remains constant and unchanged throughout 
the program's execution.
"""
print()
new_set = set(odd_num_list)
print(f"New Odd Set Numbers: {new_set}")
new_set.add(100)
new_set.add(200)
new_set.add(300)
print(f"Updated Set Numbers: {new_set}")
f_set = frozenset(new_set)
print(f"Frozen Set: {f_set}")
#f_set.remove(2)
#f_set.pop()
#f_set.add(400)
print(f"Updated Frozen Set: {f_set}")
"""
A set is a mutable, unordered collection of distinct elements that
allows for the addition or removal of elements using methods.
Set elements cannot be duplicated, and they do not follow a specific order.

A frozenset is an immutable variant of a set. Once a frozenset is created,
it cannot be modified, and its elements cannot be changed.
"""