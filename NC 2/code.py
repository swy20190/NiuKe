n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]
answer = 0
max_dp = 0
for i in range(1, len(arr)):
    if i!=1:
        max_dp = max(max_dp, dp[i-2])
    answer = max(answer, max_dp+arr[i])
    dp.append(max_dp+arr[i])

print(answer)