arr = list(map(float, input().split()))

sum_num = 0
cnt = 0


for i in arr:
    sum_num += i
    cnt += 1
avg = sum_num / cnt
print(f'{avg:.1f}')