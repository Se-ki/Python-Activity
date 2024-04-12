import datetime

t_date = {datetime.date.today().day}

s_date = {6, 7,10, 17, 87, 24, 26}

b_month = int(input("Enter Month of Birth #: "))
b_day = int(input("Enter Day of Birth #: "))
b_year = int(input("Enter Year of Birth Last Two #:"))

s_date.add(b_month)
s_date.add(b_day)
s_date.add(b_year)

print("PIN Date:", s_date.union(t_date))