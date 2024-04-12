# Python Simulation 20
# Working with Python Module

#importing created module
print()
import calc

print("Sum of Two Numbers plus 3:")
print(calc.sum(5,3), end="\n\n")

#importing other modules
import random

rand_num = random.choice(range(1,6))
print("Generated Random Number:", rand_num)

print()
result = calc.sum(rand_num, rand_num*2)
print(f"Result: {result}")

#renaming of modules
print()
import math
power = math.pow(4,2)
print(power, type(power), sep="\t", end="\n\n")

import math as math_calc
expo = math_calc.pow(3,2)
print(expo)

#accessing module selecting a particular function
print()
from new_calc import sum, average

total = sum(10, 20)
ave = average(5, 10)
print(f"The total is {total}.")
print(f"The average is {ave}.", end="\n\n")

"""
diff = diff(total, ave)
print(f"The difference is {diff}.")
NameError: name 'diff' is not defined
"""

#importing all of a module's function
print()
from new_calc import *

t = sum(2,3)
d = diff(2,3)
pr = prod(2,3)
q = quot(2,3)
a = average(2,3)
po = power(2,3)

print(f"Difference = {d}")