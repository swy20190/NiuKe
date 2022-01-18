n, q = list(map(int, input().split()))
arr = list(map(int, input().split()))
dp = [0, arr[0]]
for i in range(1, n):
    dp.append(dp[i]+arr[i])
for i in range(q):
    start, end = list(map(int, input().split()))
    print(dp[end]-dp[start-1])