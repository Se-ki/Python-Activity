num1 = 1
num2 = int(input('Enter a number: ')) 

addition_result = num1 + num2
substract_result = addition_result - .5
multiply_result = substract_result * .5
division_result = multiply_result / .5
modulo_result = division_result % .5
exponent_result = modulo_result ** .5

print("Result: ")
print("Addition = " + str(addition_result), id(addition_result), sep=" memory address ===> ")
print("Substract = " + str(substract_result), id(substract_result), sep=" memory address ===> ")
print("Multiply = " + str(multiply_result), id(multiply_result), sep=" memory address ===> ")
print("Divide = " + str(division_result), id(division_result), sep=" memory address ===> ")
print("Modulo = " + str(modulo_result), id(modulo_result), sep=" memory address ===> ")
print("Exponent = " + str(exponent_result), id(exponent_result), sep=" memory address ===> ")
