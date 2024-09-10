N = int(input())

total_sum = 0
cnt = 0

for i in range(N):
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    
    avg = total_sum / 4
    if avg >= 60:
        cnt += 1
        print("pass")
    else:
        print("fail")

print(cnt)