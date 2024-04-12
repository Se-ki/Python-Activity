from use import games, generate, vowel

b_month = int(input("Enter Month of Birth #: "))
b_day = int(input("Enter Day of Birth #: "))
b_year = int(input("Enter Year of Birth Last Two #:"))

print(generate.pin(b_month, b_day, b_year))

string = input("Enter a string: ")
index = int(input("Enter an index number: "))

vowel.checker(string, index)