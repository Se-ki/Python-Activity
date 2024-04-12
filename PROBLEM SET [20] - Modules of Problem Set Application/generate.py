def passcode(fname: str, lname: str, dayOfBirth: int, monthOfBirth: int):
    d_pass = "$2y$10$GetyygAFZOu638paeCxB3O91stUH"
    f_n_l = lname[0] + lname[-1]
    trans_data = str.maketrans("aeiou", "@#$*&")
    b_day_slice = d_pass[0:dayOfBirth]
    iter_name = '@'.join(fname)
    with_my_name = iter_name + b_day_slice
    new_last_name = lname.strip(str(f_n_l))
    con_with_lname = new_last_name + with_my_name
    b_year_slice = con_with_lname[-35:-monthOfBirth]
    no_vowels = b_year_slice.translate(trans_data)
    new_pass = no_vowels
    return new_pass
