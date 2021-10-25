def fact(number):
    return 1 if (number == 0 or number == 1) else number * fact(number - 1)

num = float(input('Please enter a number: '))
result = fact(num)

print(f'The factorial of {num} is {result}')