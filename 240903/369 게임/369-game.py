n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 or 3 in i or 6 in i or 9 in i:
        print(0, end = ' ')
    else:
        print(i, end = ' ')