# Python Simulation 02
# Working with Data Types and Operators

#getting the user input
print()
text = input()  #reading line of text from user via console/terminal
print("You've entered:", text)

print()
name = input("Enter name: ")
print("Hello", name, end="\n\n")

#taking string then converting to int
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
result = n1 + n2
print("Result =", result, end="\n\n")

#returning type from the input function
print("Data Type of name is", type(name))
age = input("Enter age: ")
print("Age data type is", type(age))
age_ = int(input("Age: "))
print("Age data type is", type(age_))

#identify class name or data types
print()
print(type(26))
print(type(2.123125412))
print(type("Azaliah"), end="\n\n")

#exploring python's dynamic data types
a = 43
b = 51231.2341
c = "42"
d = True
print(a, type(a), sep=" is a ")
print(b, type(b), sep=" is a ")
print(c, type(c), sep=" is a ")
print(d, type(d), sep=" is a ")

#working with the + operator
print()
num1 = 5
num2 = 3
print(num1, " + ", num2, " = ", num1+num2)  #addition
str1 = "Hello"
str2 = "World"
print(str1, " + ", str2, " = ", str1+str2)  #concatenation
#print(str1, " + ", num2, " = ", str1+num2)

#examining data types of mathematical operation
print()
n1 = 23
n2 = 3
r1 = n1 + n2
r2 = n1 - n2
r3 = n1 * n2
r4 = n1 / n2
r5 = n1 // n2
r6 = n1 % n2
r7 = n1 ** n2
print(n1, type(n1), n2, type(n2), sep="\n")
print(n1, "+", n2, "=", r1, "is a", type(r1))
print(n1, "-", n2, "=", r2, "is a", type(r2))
print(n1, "*", n2, "=", r3, "is a", type(r3))
print(n1, "/", n2, "=", r4, "is a", type(r4))
print(n1, "//", n2, "=", r5, "is a", type(r5))
print(n1, "%", n2, "=", r6, "is a", type(r6))
print(n1, "**", n2, "=", r7, "is a", type(r7))

#using a digit grouping symbol
print()
n1 = 12312541231
print("n1 is equal to", n1, type(n1))
n2 = 12_312_541_231
print("n2 is equal to", n2, type(n2))

#identifying object's location
print()
name = "Maria"
age = 36
print(name, id(name), sep=" ==> ")
print(age, id(age), sep=" ==> ")

#same literal value
print()
num1 = 4
num2 = num1
num3 = 26-22
print(num1, id(num1), sep=" is at ")
print(num2, id(num2), sep=" is at ")
print(num3, id(num3), sep=" is at ")

#exploring the number systems
print()
binary_num = 0b1001
print(binary_num, "= 1001", type(binary_num))
octal_num = 0o212
print(octal_num, "= 212", type(octal_num))
hex_num = 0xA1
print(hex_num, "= A1", type(hex_num))

#single line statement with multiple variables
print()
d1, d2, d3 = 24, 14, 16
print("d1 =", d1)
print("d2 =", d2)
print("d3 =", d3)

print()
d4, d5, d6 = 21, "Python", False
print("d4 =", d4)
print("d5 =", d5)
print("d6 =", d6)