number1 = float(input('Please enter a number: '))
number2 = float(input('Please enter another mumber: '))
action = input('Chose action: +, -, *, /, q - quit  ')

while action is not 'q':
    if action == '+':
        print(number1 + number2)
    if action == '-':
        print(number1 - number2)
    if action == '*':
        print(number1 * number2)
    if action == '/':
        print(number1 / number2)
    action = input('Chose action: +, -, *, /, q - quit'  )