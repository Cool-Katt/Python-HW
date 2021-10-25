def bracket_balance(ch, i=0, count=0):
    if i == len(ch): return count == 0
    if count < 0: return False
    if ch[i] == "(": return  bracket_balance(ch, i + 1, count + 1)
    elif ch[i] == ")": return  bracket_balance(ch, i + 1, count - 1)
    return bracket_balance(ch, i + 1, count)

input = '()()((())'
print(f'The sequence {input} is balanced: {bracket_balance(input)}')