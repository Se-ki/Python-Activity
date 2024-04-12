num1 = 1
num2 = int(input('Enter a number: ')) 

addition_result = num1 + num2
substract_result = addition_result - .5
multiply_result = substract_result * .5
division_result = multiply_result / .5
modulo_result = division_result % .5
exponent_result = modulo_result ** .5


_dict = {
    id(addition_result) : addition_result,
    id(substract_result) : substract_result,
    id(multiply_result) : multiply_result,
    id(division_result) : division_result,
    id(modulo_result) : modulo_result,
    id(exponent_result) : exponent_result,
}
print(_dict)