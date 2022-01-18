n, a, b, c = list(map(int, input().split()))
s = input()
dp = [0]*(n+1)
for i in range(4, n+1):
    dp[i] = dp[i-1]
    if i-4>=0:
        if s[i-4:i]=="nico":
            dp[i] = max(dp[i-4]+a, dp[i])
    if i-6>=0:
        if s[i-6:i] == "niconi":
            dp[i] = max(dp[i-6]+b, dp[i])
    if i-10>=0:
        if s[i-10:i] == "niconiconi":
            dp[i] = max(dp[i-10]+c, dp[i])

print(dp[-1])