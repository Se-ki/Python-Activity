import operator

time = 3
distance = 165
fvelocity = 10
ivelocity = 0
mass = 100
volume = 47
velocity = 5

_as = operator.truediv(distance, time)
a = operator.truediv(operator.sub(fvelocity, ivelocity), time)
density = operator.truediv(mass, volume)
force = operator.mul(mass, a)
ke = operator.mul(1/2, (operator.mul(mass, operator.pow(velocity, 2))))

ans = (_as, a, density, force, ke)
print(f"Average Speed: {ans[0]:.2f}v\nAccelerator: {ans[1]:.2f}a\nDensity of  a material: {ans[2]:.2f}rho(ρ)\nForce: {ans[3]:.2f}F\nKinetic Energy: {ans[4]}KE")
