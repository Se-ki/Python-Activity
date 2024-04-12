fname = "ChristianKyle"
lname = "Autor"
d_pass = "$2y$10$GetyygAFZOu638paeCxB3O91stUH"
trans_data = str.maketrans("aeiou", "@#$*&")
b_day_slice = d_pass[0:14]
iter_name = '@'.join(fname)
with_my_name = iter_name + b_day_slice
new_last_name = lname.strip("Ar")
con_with_lname = new_last_name + with_my_name
b_year_slice = con_with_lname[-35:-3]
no_vowels = b_year_slice.translate(trans_data)
new_pass = no_vowels

print("My new passcode is", new_pass)