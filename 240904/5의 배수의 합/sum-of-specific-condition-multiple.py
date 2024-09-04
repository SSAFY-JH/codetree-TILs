a, b = map(int, input().split())
if a < b:
    cnt = 0
    for i in range(a, b+1):
        if i % 5 == 0:
            cnt += i
    print(cnt)
else:
    cnt = 0
    for i in range(b, a+1):
        if i % 5 == 0:
            cnt += i
    print(cnt)