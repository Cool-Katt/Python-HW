operands = {
       '+': lambda a, b: a + b,
       '-': lambda a, b: a - b,
       '*': lambda a, b: a * b,
       '/': lambda a, b: a / b,
       '**': lambda a, b: a / b,
       '//': lambda a, b: a / b,
   }

while True:
    try:
        op = input('Select an operand from +, -, *, /, **, // or press q to quit:').lower()
        if op == 'q':quit()
        number1 = float(input('Prease enter a number:'))
        number2 = float(input('Please enter another number:'))
        result = operands[op](number1, number2)

    except KeyError as e:
        print(f'Invalid operation:{e}')
    except ValueError as e:
        print(f'Invalid number:{e}')
    except Exception as e:
        print(f'Unknown error: {e}')
    else:
        print(f'{number1} {op} {number2} = {result}')
        continue

