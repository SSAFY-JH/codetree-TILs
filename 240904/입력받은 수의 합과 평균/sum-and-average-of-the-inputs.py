n = int(input())

total_sum = 0

for i in range(n):
    num = int(input())
    total_sum += num

avg = total_sum / n

print(f"{total_sum} {avg:.1f}")