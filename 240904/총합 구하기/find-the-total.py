a, b = map(int, input().split())

totla_sum = 0

for i in range(a, b+1):
    if i % 6 == 0 and i % 8 != 0:
        totla_sum += i

print(totla_sum)