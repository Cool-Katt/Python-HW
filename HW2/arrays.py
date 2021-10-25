def arraySum(List):
    return sum([arraySum(i) for i in List]) if isinstance(List, list) else List

input = [1,2,3,[5,6,[7],4]]
print(f'The sum of {input} is: {arraySum(input)}')
