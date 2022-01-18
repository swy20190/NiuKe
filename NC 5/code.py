n = int(input())
string = input()
dp = []
for i in range(26):
    dp.append([0]*n)
for i in range(n-1):
    for j in range(26):
        dp[j][n-2-i] = dp[j][n-1-i]
    dp[ord(string[n-1-i])-ord('a')][n-2-i] += 1

answer = 0
for i in range(n-2):
    for j in range(26):
        if ord(string[i])-ord('a') != j:
            times = dp[j][i]
            answer += times*(times-1)/2

print(int(answer))