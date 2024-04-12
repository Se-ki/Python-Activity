first_name = "Christian Kyle"
last_name = "Autor"
gender = "Male"
age = 20
address = "Cabadbaran City"
postal_code = 8605
status = "single"
phone_number = 3453453424
birthday = "March 14, 2003"
birth_place = "Cebu City"
course = "Bachelor of Science in Information Technology"
sports = "Basketball"
idol = "Park Jimin"
hobbies = "Playing mobile legends"
favorite_color = "Black"
favorite_song = "Standing Next to you"
favorite_movies = "Avengers"
favorite_series = "Juan Dela Cruz"
favorite_programming_language = "Python"
favorite_brand = "Oxygen"

print("\n", "PERSONAL PROFILE", sep="\t\t", end="\n\n")
print("Firstname:", first_name, sep="\t\t\t\t", end="\n\n")
print("Lastname:", last_name, sep="\t\t\t\t", end="\n\n")
print("Gender:", gender, sep="\t\t\t\t\t", end="\n\n")
print("Age:", age, sep="\t\t\t\t\t", end="\n\n")
print("Address:", address, sep="\t\t\t\t", end="\n\n")
print("Postal Code:", postal_code, sep="\t\t\t\t", end="\n\n")
print("Status:", status, sep="\t\t\t\t\t", end="\n\n")
print("Phone Number:", phone_number, sep="\t\t\t\t", end="\n\n")
print("Birthday:", birthday, sep="\t\t\t\t", end="\n\n")
print("Birth Place:", birth_place, sep="\t\t\t\t", end="\n\n")
print("Course:", course, sep="\t\t\t\t\t", end="\n\n")
print("Sports:", sports, sep="\t\t\t\t\t", end="\n\n")
print("My Idol:", idol, sep="\t\t\t\t", end="\n\n")
print("Hobbies:", hobbies, sep="\t\t\t\t", end="\n\n")
print("My Favorite Color:", favorite_color, sep="\t\t\t", end="\n\n")
print("My Favorite Song:", favorite_song, sep="\t\t\t", end="\n\n")
print("My Favorite Movies:", favorite_movies, sep="\t\t\t", end="\n\n")
print("My Favorite Series:", favorite_series, sep="\t\t\t", end="\n\n")
print("My Favorite Brand:", favorite_brand, sep="\t\t\t", end="\n\n")
print("My Favorite Programming Language:", favorite_programming_language, sep="\t", end="\n\n")


text_file = open('profile.txt', 'w')
print("PERSONAL PROFILE"
      "\nFirstname: ", first_name, 
      "\nLastname: ", last_name,
      "\nGender: ", gender,
      "\nAge: ", age,
      "\nAddress: ", address,
      "\nPostal Code: ", postal_code,
      "\nStatus: ", status, 
      "\nPhone Number: ", phone_number, 
      "\nBirthday: ", birthday, 
      "\nBirth Place: ", birth_place, 
      "\nCourse: ", course, 
      "\nSports: ", sports, 
      "\nMy Idol: ", idol, 
      "\nHobbies: ", hobbies, 
      "\nMy Favorite Color: ", favorite_color, 
      "\nMy Favorite Song:", favorite_song,
      "\nMy Favorite Movies:", favorite_movies,
      "\nMy Favorite Series:", favorite_series,
      "\nMy Favorite Brand:", favorite_brand,
      "\nMy Favorite Programming Language:", favorite_programming_language, file=text_file)
text_file.close()
