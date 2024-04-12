# Python Simulation 15-02

#importing a function from different file inside a package
print()

from mypackage import power, average, greet

hw = greet("world!")
rp = power(3,2)
print(f"3 raise to the power of 2 is {rp}")
ra = average(rp,1)
print("Average:", ra)
print()