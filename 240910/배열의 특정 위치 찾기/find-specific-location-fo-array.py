arr = list(map(int, input().split()))

n = len(arr)

result = sum(arr[1:n:2])

avg = result / 5

print(result, round(avg, 2))