def generate_numbers(num):
    for i in str(num):
        yield int(i)

def print_split(gen):
    for i in range(0, len(str(integer))):
        print(next(gen))


integer = int(input('Please enter an integer number: '))
split = generate_numbers(integer)

print_split(split)