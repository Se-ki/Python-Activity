def pin(b_month, b_day, b_year):
    import datetime
    t_date = {datetime.date.today().day}
    s_date = {6, 7,10, 17, 87, 24, 26}
    s_date.add(b_month)
    s_date.add(b_day)
    s_date.add(b_year)
    return s_date.union(t_date)