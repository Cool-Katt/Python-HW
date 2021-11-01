from functools import wraps

def remove_duplicates(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__original = func
        args = [set(el) for el in args]
        return func(*args, **kwargs)
    return wrapper

def sum_arr(arr):
    return print(f'Sum = {sum(arr)}')

arr = [1,2,3,4,1,2,3,4,5]
print(f'Original array: {arr}')
print(f'Sum of original array:')
sum_arr(arr)
sum_arr = remove_duplicates(sum_arr)
print(f'Sum of processed array:')
sum_arr(arr)
print(f'Original func:')
sum_arr.__original(arr)
