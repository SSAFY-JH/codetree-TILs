arr = list(map(int, input().split()))
sum_num = 0
cnt = 0

for i in arr:
    if i >= 250:
        break
    sum_num += i
    cnt += 1

avg = sum_num / cnt

print(f'{sum_num} {avg:.1f}')