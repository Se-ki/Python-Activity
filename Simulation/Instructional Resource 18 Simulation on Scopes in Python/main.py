# Python Simulation 18
# Exception Handling

#Index Error
print()
num_list = [1,2,3]
print(num_list)
print(num_list[1])
#print(num_list[5]) IndexError: list index out of range
print()

#ModuleNotFoundError
#import whatever    No module named 'whatever'

#KeyError
print()
my_dict = {1:"One", 2:"Two", 3:"Three"}
print(my_dict)
print(my_dict[3])
#print(my_dict[9])  KeyError: 9

#ImportError
print()
#from math import science   ImportError: cannot import name 'science'

#StopIteration
iter_name = iter(["Junell", "Maria", "Hannah", "Elisha"])
print(next(iter_name))
print(next(iter_name))
print(next(iter_name))
print(next(iter_name))
#print(next(iter_name))     StopIteration

#TypeError
print()
calc1 = 2 + 3
print(calc1)
#calc2 = "7" + 5    TypeError: can only concatenate str (not "int") to str

#ValueError
print()
print(int(12.5))
#print(int("Python"))   ValueError: invalid literal for int() with base 10: 'Python'

#NameError
print()
name = "Junell"
print(f"Name: {name}")
#print(f"Age: {age}")   NameError: name 'age' is not defined

#ZeroDivisionError
print()
print(12/4)
#print(12/0)    ZeroDivisionError: division by zero

#try and except block
print()
try:
    n1 = 23
    n2 = "7"
    print(n1/n2)
except:
    print("There is an error!")

#catching a specific error type
print()
try:
    a=5
    b='0'
    print(a+b)
except TypeError:
    print("Unsupported Operation!")

#multiple except
print()
try:
    n1 = 4
    n2 = "5"
    n3 = 2
    print(n1+n2)
    print(n1-n2)
    print(n1*n3)
    print(n1/0)
except IndexError:
    print("There is an index error!")
except ZeroDivisionError:
    print("There is a zero division error!")
except KeyError:
    print("There is a key error")
except TypeError:
    print("There is a type error!")
    n1 = int(n1)
    n2 = int(n2)
    print(n1+n2)
    print(n1-n2)
    print(n1*n2)
except ValueError:
    print("There is a value error!")

#else and finally
print()
try:
    x = int(input("First Number: "))
    y = int(input("Second Number: "))
    result = x/y
except ZeroDivisionError:
    print("Division of zero is not accepted!")
else:
    print("The result is", result, end="\n\n")
finally:
    x=0; y=0
    print(f"x = {x}\ny = {y}")

#raise an exception
print()
try:
    num = int(input("Enter a number up to 100: "))
    if num>100:
        raise ValueError(num)
except ValueError:
    print(num, "is out of allowable input number.")
else:
    print(f"The inputted {num} is within range.")
print()