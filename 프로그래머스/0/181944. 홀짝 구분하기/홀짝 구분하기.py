import operator

n = int(input())

if operator.mod(n, 2) == 0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')