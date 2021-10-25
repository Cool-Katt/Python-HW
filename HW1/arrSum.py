number = int(input('Please enter a number: '))
arr = [1, 4, 6, 8, 9, 23]
print(f'Lookup array is: {arr}')
found = False
i,k = 0,0

while not found:
    if arr[i] + arr[k] == number:
        found = True
        print(f'arr[{i}] + arr[{k}] == {number}')
    if k < len(arr) - 1:
        k += 1
    else:
        i += 1
        k = 0
    if i >= len(arr):
        print('not found')
        break
    