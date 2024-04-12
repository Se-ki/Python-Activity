import datetime

first_day = datetime.datetime(2024, 2, 3, 8, 00)
second_day = datetime.datetime(2024, 2, 4, 9, 00)

ten_Oclock = datetime.time(10, 00).strftime('%I:%M %p')
eleven_Oclock = datetime.time(11, 00).strftime('%I:%M %p')
one_Oclock = datetime.time(13, 00).strftime('%I:%M %p')
two_Oclock = datetime.time(14, 00).strftime('%I:%M %p')
four_Oclock = datetime.time(16, 00).strftime('%I:%M %p')
five_Oclock = datetime.time(17, 00).strftime('%I:%M %p')
six_Oclock = datetime.time(18, 00).strftime('%I:%M %p')
seventhirty_Oclock = datetime.time(19, 30).strftime('%I:%M %p')
nine_Oclock = datetime.time(21, 00).strftime('%I:%M %p')
tenthirty_Oclock = datetime.time(22, 30).strftime('%I:%M %p')


print()
print("\tInput your top five favorite")
print("============================================")
fav1 = str(input("My 1st favorite: "))  # coffee
fav2 = str(input("My 2nd favorite: "))  # Piattos
fav3 = str(input("My 3rd favorite: "))  # Gaming Chair
fav4 = str(input("My 4th favorite: "))  # Pakbet
fav5 = str(input("My 5th favorite: "))  # Softdrinks

print()
print("\tInput your top three hobbies or interest")
print("========================================================")
hob1 = str(input("My 1st hobbies or interest: "))  # dancing
hob2 = str(input("My 2nd hobbies or interest: "))  # basketball
hob3 = str(input("My 3rd hobbies or interest: "))  # mobile legends

print()
print(f" On {first_day.strftime('%A')}, {first_day.strftime('%B %drd')}, my day kicks off at {first_day.strftime('%I:%M %p')} with a steaming cup of {fav1},\n my all-time favorite. From {ten_Oclock} to {two_Oclock}, I immerse myself in practicing {hob1},\n a hobby I truly enjoy. At {four_Oclock}, it's {hob2} time with friends, and we play\n until {six_Oclock}, having a great time on the court. Later at {seventhirty_Oclock}, I unwind by munching\n on some {fav2} while sitting on my favorite {fav3}. By {nine_Oclock}, it's dinner, and I relish a plate\n of {fav4}, a dish that never disappoints. To cap off the night at {tenthirty_Oclock}. \n\n {second_day.strftime('%A')}, {second_day.strftime('%B %dth')}, starts a bit more leisurely with {fav1} at {second_day.strftime('%I:%M %p')}. From {eleven_Oclock}\n to {one_Oclock}, I engage in another round of {hob1} practice. After a lunch at {two_Oclock},\n I gather with friends for a friendly {hob3} session, playing until {five_Oclock}.\n The evening at {seventhirty_Oclock} is dedicated to enjoying my favorite {fav5} while watching\n more entertaining content sitting on my favorite {fav3}. By {nine_Oclock}, dinner consists of the flavorful\n {fav4} I adore. Finally, at {tenthirty_Oclock}, I wrap up the weekend, looking forward to the\n simple joys that fill my days.")
print()

text_file = open("paragraph.txt", 'w')
print(f" On {first_day.strftime('%A')}, {first_day.strftime('%B %drd')}, my day kicks off at {first_day.strftime('%I:%M %p')} with a steaming cup of {fav1},\n my all-time favorite. From {ten_Oclock} to {two_Oclock}, I immerse myself in practicing {hob1},\n a hobby I truly enjoy. At {four_Oclock}, it's {hob2} time with friends, and we play\n until {six_Oclock}, having a great time on the court. Later at {seventhirty_Oclock}, I unwind by munching\n on some {fav2} while sitting on my favorite {fav3}. By {nine_Oclock}, it's dinner, and I relish a plate\n of {fav4}, a dish that never disappoints. To cap off the night at {tenthirty_Oclock}. \n\n {second_day.strftime('%A')}, {second_day.strftime('%B %dth')}, starts a bit more leisurely with {fav1} at {second_day.strftime('%I:%M %p')}. From {eleven_Oclock}\n to {one_Oclock}, I engage in another round of {hob1} practice. After a lunch at {two_Oclock},\n I gather with friends for a friendly {hob3} session, playing until {five_Oclock}.\n The evening at {seventhirty_Oclock} is dedicated to enjoying my favorite {fav5} while watching\n more entertaining content sitting on my favorite {fav3}. By {nine_Oclock}, dinner consists of the flavorful\n {fav4} I adore. Finally, at {tenthirty_Oclock}, I wrap up the weekend, looking forward to the\n simple joys that fill my days.", file=text_file)
text_file.close()

