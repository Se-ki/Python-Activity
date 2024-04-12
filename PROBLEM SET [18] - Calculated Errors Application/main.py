num1 = int(input("Num 1: ")) 
num2 = int(input("Num 2: "))
try:
    import operator
    div = operator.truediv(num1, num2)
    add = operator.add(num1, num2)
    sub = operator.sub(num1, num2)
    mul = operator.mul(num1, num2)
    print("Total Divide = ", div)
    print("Total Addition = ",add)
    print("Total Substraction = ",sub)
    print("Total Multiplication = ",mul)
except:
    print("Error during calculation")    
    