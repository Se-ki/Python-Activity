fname = "christian kyle"
lname = "autor"
sex = "male"
age = "20"
birth_place = "cebu city"

# this line of code will capitalize the firstname and lastname
print(f"Capitalized Text: {fname.capitalize()} {lname.capitalize()}") 

# this line of code will count the letter 'c' in the string
print(f"The number of letter \"c\" in my birthplace is {birth_place.count('c')}")

# this line of code will check if the string ended with 'city'
print(f"Does my birth place ends with city? {birth_place.endswith('city')}")

# this line of code will return the index of letter 'i' in my firstname 
print(f"In my name what index is letter \"i\"? it is {fname.index('i')}.")

# this line of code it will find the leter 'd' in my lastname if not found it will return -1
print(f"Can you find a letter \"d\" in my last name? {lname.find('d') != -1}")

# this line of code will check if the value of age is a digit
print(f"Is my age a number? {age.isdigit()}")

# the 'center' method will return a centered string of length width. 
print("Is my firstname and lastname capitalize?")
print("^".center(20),"^".center(8))

#the 'islower' method is the function to check if the value is in lowercase  
print(f"{not fname.islower()}".center(20), f"{not lname.islower()}".center(8))