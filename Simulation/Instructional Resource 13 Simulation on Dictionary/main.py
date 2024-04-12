# Python Simulation 13
# Dictionary in Python

#declaring a dictionary
print()
ed = {}
print(f"Empty Dictionary: {ed}")

print()
capitals = {"USA":"Washington", "France":"Paris", "India":"New Delhi"}
print(f"Country's Capital City: {capitals}")

print()
numNames = {1:"One", 2:"Two", 3:"Three"}
print(f"Number Names: {numNames}")

print()
decNames = {1.5:"One and Half", 2.5:"Two and Half", 3.5:"Three and Half"}
print(f"Fractional Numbers: {decNames}")

print()
items = {
            ("Parker", "Reynolds", "Camlin"):"PEN",
            ("LG", "Whirlpool", "Samsung"):"FRIDGE"
        }
print(f"My Items:\n{items}")

print()
my_objects = {
                "Fruits":["Mango", "Bananas", "Apples"],
                "Colors":["Blue", "Red", "Green"]
            }
print(f"My Objects: {my_objects}", end="\n\n")

#creating a dictionary
print()
empty_dict = {}
initial_dict = {"key":"value", 1:"One", "Fractional":24.15}
copy_key_dict = {*initial_dict}     #unordered copy of dictionary keys
copy_kv_pair = {**initial_dict}

print(f"Empy Dictionary: {empty_dict}")
print(f"Stored Dictionary: {initial_dict}")
print(f"Copied Key Dictionary: {copy_key_dict}")
print(f"Copied Key-Value Pair Dicationary: {copy_kv_pair}")

#treatment of multiple similar items
numNames = {1:"One", 2:"Two", 3:"Three", 2:"Two", 1:"One"}
print(f"Number Names: {numNames}")

#examine the class types
print()
print(numNames, type(numNames), sep=" --> ")

#accessing values in a dictionary
print()
capitals = {"USA":"Washington", "France":"Paris", "India":"New Delhi"}
print(f"Country's Capital City: {capitals}")
print(capitals["USA"])
print(capitals["India"])

#using the get() in accessing the dictionary value
print()
print(capitals.get("France"))
print(capitals.get("India"))

#accessing dictionary using for loop
print()
capitals = {"USA":"Washington", "France":"Paris", "India":"New Delhi"}
print(capitals, "\n")

for key in capitals:
    print("Key = " + key + ", \tValue = " + capitals[key])

#updating a dictionary
print()
student_grade = {"Junell":85, "Maria":91, "Hannah":90}
print(f"Student Grades: {student_grade}")
student_grade["Junell"] = 81
print(f"New Grades: {student_grade}")

#adding a new key-value pair
print()
student_grade["John"] = 87
student_grade["New Student"] = 99
print(f"Updated Student Grades: {student_grade}")

#deleting key-value pair in dictionary
print()
del student_grade["John"]
print(f"Updated Student Grades: {student_grade}")

#combining dictionaries
print()
avenger1 = {
                "Captain Marvel":"Carol Danvers",
                "Captain America":"Steve Rogers",
                "Black Widow":"Natasha Romanoff"
        }
avenger2 = {
                "Iron Man":"Mark1",
                "Hulk":"Smash",
                "Thor":"Hammer"
        }
avenger3 = {
                "Ant-Man":"Ant",
                "Spider Man":"Spider"
        }
print(avenger1, avenger2, avenger3, sep="\n\n")
print()
avengers_assemble = {1:avenger1, 2:avenger2, 3:avenger3}
print(avengers_assemble, end="\n\n")

#accessing combined dictionary data
print()
print(avengers_assemble[1])
print(avengers_assemble[1]["Black Widow"])
print()

#more on itering dictionary pairs
print()
num_names = {1:"one", 2:"two", 3:"three", 4:"four"}
print(num_names)
currency = {
                "United States":"dollar",
                "Japan":"yen",
                "Philippines":"peso"
        }
print(currency)

print()
for i1 in num_names:
    print(i1)
for i1 in num_names.keys():
    print(i1, end=" ")
print()
for i2 in currency:
    print(f"The {currency[i2]} is used in the {i2}.")