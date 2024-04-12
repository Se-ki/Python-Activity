# Python Simulation 01
# Python General Syntax

#print() display text or values
print("Hello World!!!")
print("Employee ID:", 123)
print("First Name:", "Junell")
print("Last Name:", "Bojocan")

#calling an argument-less print()
print()

#splitting a lone line of code into multiple lines
print("I am learning python programming!!! \
Python is fun and easy to learn.")

#breaking code statement into multiple code lines for readability
print()
if (100>99) and \
    (200<=500) and \
    (True!=False):
    print("That's nice!!!")

#using semicolon ; to separate statements in a single code line
print(); print("edi wow")
print("num1 =", 2); print("num2 =", 12); print("num3 =", 26)

#populating data collection over multiple lines for readability
print()
myNumList = [1, 2, 3,
             4, 5, 6,
             7, 8, 9,
             10]
print(myNumList)

print()
myItems = ("MacBook Ari", "IPhone 8+",
           "Technopack", "Umbrella")
print(myItems)

#python indentation with if statements
print()
if (10>5):
    print("10 is greater than 5.")
    print("Checking if 20 is greater than 10.")
    if (20>10):
        print("That is correct!")
else:
    print("10 is less than 5.")
    print("This seems wrong!")

#python indentation with function statement
print()
def your_name(name):
    print("Hello", name)
    print("Welcome to python programming!!!\n")

your_name("Junell")
your_name("Rico")
your_name("Kyle")

#working with comments
print()
print("Comments are use to label code statements or blocks.")
print("Use the # to denote a comment.") #this here is a comment

#working with multi-line comment
"""
In python, there is no provision to write multi-line
comments, or a block comment. A triple quoted multi-line string
is also treated as a comment if it is not a docstring of the
function or the class. 
"""

#docstrings stored as an attribute accessed programmatically
print()
def myDocFunction():
    """This is an example of a eufee buang."""
    return
print(myDocFunction.__doc__)

#more on the docstring
print()
def message(name, greetings="Welcome to python"):
    """   
        printing of greetings to the user names
        the greetings here has an initial string data.
    """
    print("{} {}.".format(greetings, name))
    #      ^  ^
    #     so kani silang duha is mao ni insertan sa mga value nga greetings og name
message("Christian Kyle")
print(message.__doc__)

print()
class Greetings:
    """An object used to greet people.
    It contains multiple greeting function for
    several languages and time of the day.
    """
print(Greetings.__doc__)

print()
def learning(name, message):
    """This function prints the name and a message.

    Arguments:
    name: the name of a person
    message: text message for the person
    """
    print(f"Hello {name}, {message}.")
    
print(learning.__doc__)
learning("Wilmar", "you are learning python")
learning("Joselito", "is enjoying python programming")

#Sphinx formatting of a docstring
print()
def favFruits(name, fruit, quantity):
    """This function prints a person's favorite fruit

    :param name: the name of a person
    :type name: str
    :param fruit: the favorite fruit of a person
    :type fruit: str
    :param quantity: the number of fruits eaten by a person
    :type quantity: int
    """
    print(f"{name} likes to eat {quantity} {fruit}'s.")

print(f"favFruits Docstring:\n{favFruits.__doc__}")
favFruits("Sheila", "Apple", 3)
favFruits("Rodalyn", "Banana", 4)
print()

#Google Python Style Guide formatting of a docstring
print()
def myBDay(name, month, day, year):
    """This function prints the birthday details of a person.

    Args:
        name: the name of a person
        month: the birthday month
        day: the day of birth
        year: the birth year

    Returns:
        A birthday details.
    """
    birth = f"{name}'s birthdate is on {day}:{month}:{year}."
    return birth

print(f"myBDay Docstring:\n\n{myBDay.__doc__}")
print(myBDay("Jessiel", 9, 19, 2001))

#the print() function for display and more
print()
name = "Junell"
print(name)
age = 36
print(name, age)
print("\nName:", name, "\nAge:", age)
print(f"My name is {name}, and I am {age} years old.")

#content control display under the print() function
print("\nI am learning python programming.")
print("\nI \nam \nlearning \npython programming.")
print("A text apart?")
print("\tA \ttext \tapart\t?")

#treating escape sequences as literal characters
print()
print("c:\some_file\name")
print(r"c:\some_file\name")

#working with other paramaters under the print() fucntion
print()
print("I am", name, "python is new to me.")
print("I am", name, "python is new to me.", sep="-->", end="\n\n")
print("I am", name, "python is new to me.", sep="______", end="\n\n")

#multiple variable data calls to be printed
print()
print("", "PERSONAL PROFILE", sep="\t", end="\n\n")
c_name = "Junell T. Bojocan"
gender = "Male"
age = 36
mob_num = 123124123123
print("Name:", c_name, sep="\t\t", end="\n\n")
print("Gender:", gender, sep="\t\t", end="\n\n")
print("Age:", age, sep="\t\t", end="\n\n")
print("Mobile Number:", mob_num, sep="\t", end="\n\n")

#passing data into a text file with print()
text_print = open("sample.txt", "w")
print("Good afternoon everyone! Mag kape ko taod2x!!!", file=text_print)
text_print.close()

content = "I am learning python programming."
text_print2 = open("sample2.txt", "w")
print("Hi, I am", c_name, \
      " and I am", age, \
      "years old.", content, \
      sep=" ", file=text_print2)
text_print2.close()
