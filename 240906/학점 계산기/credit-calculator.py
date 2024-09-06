n = int(input())
score = list(map(float, input().split()))

total = 0

for i in range(n):
    total += score[i]

avg = total/n
print(f'{avg:.1f}') 

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")