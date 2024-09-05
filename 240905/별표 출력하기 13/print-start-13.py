n = int(input())

for i in range(n):
    if i % 2 == 0:
        for j in range(n - i):
            print('*', end = " ")
        print()
    else:
        print('*')