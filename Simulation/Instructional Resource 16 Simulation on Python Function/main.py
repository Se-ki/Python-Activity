# Python Simulation 16
# Python Function

#user-defined function
print()
def message():
    """This function prints a message"""
    print("Hello World!!!")
    print("I am learning python.")
    print("Thank you!!!")
message()   #calling the defined function
message()
message()

#assigned a user-defined function
print()
def fav_fruits():
    print("Apples, Mango, and Oranges.\n")
f = fav_fruits()
print(f, end="\n\n")

#defining a function to received data for processing
def message(name):
    print("Hello", name, end="\n\n")
message("Junell")
message("Maria")
message(123)

#multiple parameters in function
print()
def gospel(g1,g2,g3,g4):
    print("Christ's Apostles:", g1,g2,g3,g4, sep="\n", end="\n\n")
gospel("Luke", "Mark", "Matthew", "John")

#defining a function with unknown number of arguments
def apostles(*a):
    print(f"Christ's Apostles: {a[0]}, {a[1]}, {a[2]}")
apostles("Simon", "Peter", "John", "Thomas", "Jude")

#getting the sum of numbers
print()
def get_sum(*n):
    sum = 0
    for num in n:
        sum += num
    return sum
print(f"The sum is {get_sum(1,2,3)}")
print(f"The sum is {get_sum(2,3,5123,2,9,5)}")

#more on function; variable as argument
print()
def access(un, pw):
    print("Username:", un)
    print("Password:", pw)
uname = "jtbojocan"
pword = "admin"
access(uname, pword)

#receiving excess through prefixing **
print()
def names(**person):
    print("Hello", person["fname"], person["lname"])
names(fname="Junell", lname="Bojocan")
names(fname="Maria", lname="Bojocan", age=35)
#names(fname="Elisha")  KeyError: 'lname'

#using the function's default value
print()
def number(num=35):
    print(f"Num = {num}")
number(15)
number(523)
number()

#functions with return value
print()
def total(n1,n2):
    return n1+n2
result = total(10, 23)
print(f"The sum is {result}")
result = total(12.32, 1.52)
print(f"Sum = {result}")

#the lambda function
print()
def sqr(x):
    return x*x
r1 = sqr(5)
print(f"The square of 5 is {r1}")

sqr2 = lambda x: x*x+1
res = sqr2(5)
print(f"\nThe square of 5 is {res}")

calc_total = lambda n1,n2: n1+n2
r2 = calc_total(10,32)
print(f"The calculated total is {r2}")

message = lambda name: print("Hello", name)
message("Junell")
message("Maria")