total_age = 0
cnt = 0

while True:
    age = int(input())
    if age < 30:
        total_age += age
        cnt += 1
    if age >= 30:
        break
print(f"{total_age / cnt:.2f}")