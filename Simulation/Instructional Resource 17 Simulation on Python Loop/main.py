# Python Simulation 17
# Scopes in Python

#local variable in a function
print()
def message():
    name = "Junell"
    print(f"Hello {name}")
message()
#print(name)    NameError: name 'name' is not defined

#working with global variable for a function
print()
name = "Maria"
def message():
    print("Name:", name)
message()
print(name)

#utilizing local and global variable, the same identifier
print()
age = 36
def my_age():
    age = 29
    print("Age:", age)
my_age()
print(f"I am {age} years old.")

#changing the data of global variable from within a function
print()
email = "junellbojocan@aclcbutuan.edu.ph"
print(f"Email: {email}")

def my_email():
    global email
    email = "jtbojocan@gmail.com"
    print(f"My Email: {email}")
my_email()
   
print(f"My email address is {email}")