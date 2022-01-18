n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
for i in range(1, n):
    if dp[i-1]>0:
        dp.append(arr[i]+dp[i-1])
    else:
        dp.append(arr[i])
answer = dp[0]
for i in dp:
    answer = max(i, answer)
print(answer)