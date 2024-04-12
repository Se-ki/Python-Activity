# Python Simulation 21-01

# importing a module from a directory/package
print()

from mypackage import my_calc

rp = my_calc.power(3,2)
print(f"Power Result: {rp}", end="\n\n")

rs = my_calc.sum(2,3)
print(f"Sum Result: {rs}", end="\n\n")

ra = my_calc.average(10,5)
print(f"Average Result: {ra}", end="\n\n")

#importing a specific function from a directory/package
from mypackage.my_calc import sum

s = sum(10,20)
print(f"10 + 20 = {s}")

"""
NameError: name 'average' is not defined
a = average(15,2)
print(a)
"""