# Python Simulation 15
# Python For Loop

#looping from a list
print()
num = [10, 20, 30, 40, 50]
for each_num in num:
    print(each_num)

#looping from a tuple
print()
name = ("Junell", "Maria", "Hannah", "Elisha")
for each_name in name:
    print(each_name, end="-->")
print()

#looping through each character in a string input
print()
text = input("Enter text: ")
for each_text in text:
    print(each_text)

#looping from a dictionary
print()
numNames = {1:"One", 2:"Two", 3:"Three"}
for pair in numNames.items():
    print(pair, type(pair), sep=" --> ", end="\n")

print()
for dict_key, dict_value in numNames.items():
    print(f"Key = {dict_key},\tValue = {dict_value}")

#looping from a range
print()
num_range = range(5)
print(num_range, type(num_range), sep=" --> ")
print("Values =", num_range[0], num_range[1], \
      num_range[2], num_range[3], num_range[4], end="\n\n")

for num in range(5):
    print(num)

#alterning for loops action
print()
stop = int(input("Stopping Number[1-10]: "))
x = 10
for i in range(x):
    print(i)
    if i==stop:
        print("ENOUGH!!!")
        break
print()

#nested for loop
for x in range(1,4):
    for y in range(1,3):
        print(f"Value of x is {x}, and value of y is {y}.")
    print()
print()

#itering multiple list items
print()
odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]

for o_num in odd:
    for e_num in even:
        prod = o_num * e_num
        print(f"{o_num} * {e_num} = {prod}")
    print()
print()

#itering items in a list and getting its total
print()
num = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

for i in num:
    print(i)
    sum = 0
    for j in i:
        print(j)
        sum += j
    print(f"The sum is {sum}\n")

#removing duplicate items in a list
print()
letters_list = ['A','a','A','b','B','C','C','c','D','D','d','a','b','c','d']
print(f"List of Letters: {letters_list}")

ls = []
for ll in letters_list:
    if ll in ls:
        del(ll)
    else:
        ls.append(ll)
print(f"Deleted Duplicate with New List: {ls}")

print()
print("Letters List: {}".format(letters_list))
for l2 in letters_list:
    lc = letters_list.count(l2)
    if lc>1:
        letters_list.remove(l2)
print("Unordered Filtered Letters: {0}".format(letters_list))

print()
my_text = list(input("Enter a text: "))
print(f"User Text: {my_text}\tText Type: {type(my_text)}")

store_list = []
print()
for s in my_text:
    if s in store_list:
        print(f"{s} has duplicate")
    else:
        store_list.append(s)

#more on itering items over a collection
print()     #[reserved for a problem set]
text_name = "Elisha Dinah Canda Bojocan"
c = 0
print(f"Complete Name: {text_name}")
name = ""
for l in text_name:
    print(f"Index[{c}] = {l}")
    c += 1
    name += l
    if c==(len(text_name)-14):
        print(f"Name: {name}")
        print("Printing only the first name!!!")
        break 
else:
    print("Done printing the complete name!!!")

print()
num = [1,2,3,4,5]
for i in num:
    if type(i) is not int:
        print(f"{i} is not integer.")
        break
else:   #if not break or if not found
    print("No exception!!!")
    print(f"{i} is the last item and an integer.")

print()
t_num = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
for i in t_num:
    i1 = i[0]
    i2 = i[1]
    i3 = i[2]
    print(i1, i2, i3, sep="\t")