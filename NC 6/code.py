n, m, q = list(map(int, input().split()))
dp = []
for i in range(n):
    raw = list(map(int, input().split()))
    line = []
    curr_sum = 0
    if i == 0:
        for j in range(m):
            line.append(curr_sum + raw[j])
            curr_sum += raw[j]
        dp.append(line)
    else:
        for j in range(m):
            line.append(curr_sum + dp[-1][j] + raw[j])
            curr_sum += raw[j]

        dp.append(line)

for i in range(q):
    x1, y1, x2, y2 = list(map(int, input().split()))
    answer = dp[x2 - 1][y2 - 1]
    if x1 != 1:
        if y1 != 1:
            answer = answer - dp[x1 - 2][y2 - 1] - dp[x2 - 1][y1 - 2] + dp[x1 - 2][y1 - 2]
        else:
            answer = answer - dp[x1 - 2][y2 - 1]
    else:
        if y1 != 1:
            answer = answer - dp[x2 - 1][y1 - 2]
    print(answer)