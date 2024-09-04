N = int(input())
class_clean = 0
hall_clean = 0
restroon_clean = 0

for i in range(1, N):
    if i % 12 == 0:
        restroon_clean += 1
    elif i % 3 == 0:
        hall_clean += 1
    elif i % 2 == 0:
        class_clean += 1
print(class_clean, hall_clean, restroon_clean)