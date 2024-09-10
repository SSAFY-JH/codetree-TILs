N = int(input())
arr = list(map(int, input().split()))

numbers = []

for i in range(N - 1, - 1, -1):
    if arr[i] % 2 == 0:
        numbers.append(arr[i])

print(*numbers)