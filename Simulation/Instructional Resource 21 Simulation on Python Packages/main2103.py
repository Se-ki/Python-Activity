# Python Simulation 21-03

#more on packages
print()

from mypackage import sum, average, power, greet

n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))

r_sum = sum(n1,n2)
r_ave = average(n1,n2)
r_pow = power(n1,n2)

print()
print(f"The total is {r_sum}.")
print(f"The average is {r_ave}.")
print(f"The power is {r_pow}.")

print()
u_name = input("Enter username: ")
greet(u_name)