n = int(input())
total = 0
for i in range(n):
    a = int(input())
    if i % 2 == 1 and i % 3 == 0:
        total += a
print(total)