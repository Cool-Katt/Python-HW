import math

def fact(number):
    return 'NaN' if (number < 0) else math.factorial(number)

num = float(input('Please enter a number: '))
result = fact(num)

print(f'The factorial of {num} is {result}')