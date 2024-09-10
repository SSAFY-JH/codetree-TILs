arr = list(map(int, input().split()))

cnt = 0
plus = 0


for i in arr:
    if i == 0:
        break
    if i % 2 == 0:
        cnt += 1
        plus += i

print(f'{cnt} {plus}')