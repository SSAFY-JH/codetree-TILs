a, b = map(int, input().split())

if b >= a:
    for i in range(b, a-1, -1):
        print(i, end= " ")
else:
    for j in range(a, b - 1, -1):
        print(j, end= " ")