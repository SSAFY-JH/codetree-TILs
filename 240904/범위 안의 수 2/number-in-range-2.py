total = 0
average = 0

for i in range(10):
    n = int(input())
    if n >= 0 and n <= 200:
        total += n
        average += 1


avg = total / average
print(f'{total} {avg:.1f})