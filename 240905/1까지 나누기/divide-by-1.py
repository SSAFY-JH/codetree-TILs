n = int(input())

cnt = 0
for i in range(n):
    if n // i <= 1:
        break
    cnt += 1
print(cnt)