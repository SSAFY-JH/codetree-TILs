arr = list(map(int, input().split()))

plus = 0
cnt = 0

for i in arr:
    if i == 0:
        break
    plus += i
    cnt += 1

result = plus / cnt

print(f'{plus} {result:.1f}')