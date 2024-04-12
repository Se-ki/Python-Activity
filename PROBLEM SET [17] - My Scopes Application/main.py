#if the variable is outside from function it will be now a global scope
name = "Christian Kyle Autor"
age = 21

# this username and password variable is a global scope
username = ""
password = ""

def credentials():
    # username and password is a local variable because it put inside a function
    username = "Christian Kyle Autor"
    password = "gwapo123"
    print(f"username: {username} \npassword: {password}")

def isLocalVarAccessible():
    if username and password: # check if I can get the value from local variable 
        print(f"username: {username} \n password: {password}")
    else: #otherwise print the name and age from the global scope
        print(name, age, sep="\n")

credentials()
isLocalVarAccessible()    