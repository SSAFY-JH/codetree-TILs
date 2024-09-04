n = int(input())
sum_result = 0
for i in range(1, 101):
    sum_result += i
    if sum_result >= n:
        print(i)
        break