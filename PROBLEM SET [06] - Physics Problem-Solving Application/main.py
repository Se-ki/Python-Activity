import operator

time = 3
distance = 165
_as = operator.truediv(distance, time)
print(f"Average Speed of a moving body {_as:.2f}")
print(type(_as), end='\n\n')

fvelocity = 10
ivelocity = 0
a = operator.truediv(operator.sub(fvelocity, ivelocity), time)
print(f"Acceleration {a:.2f}")
print(type(a), end='\n\n')

mass = 100
volume = 47
density = operator.truediv(mass, volume)
print(f"Density of a material {density:.2f}")
print(type(density), end='\n\n')

force = operator.mul(mass, a)
print(f"Force {force:.2f}")
print(type(force), end='\n\n')

velocity = 5
ke = operator.mul(1/2, (operator.mul(mass, operator.pow(velocity, 2))))
print(f"Kinetic Energy {ke:.2f}")
print(type(ke)) 
