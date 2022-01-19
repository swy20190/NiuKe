while True:
    try:
        s1 = input()
        s2 = input()
        if len(s1) == 0:
            print(len(s2))
        else:
            if len(s2) == 0:
                print(len(s1))
            else:
                dp = []
                for i in range(len(s1) + 1):
                    line = [0] * (len(s2) + 1)
                    dp.append(line)
                for i in range(len(s2) + 1):
                    dp[0][i] = i
                for i in range(len(s1) + 1):
                    dp[i][0] = i
                for i in range(1, len(s1) + 1):
                    for j in range(1, len(s2) + 1):
                        if s1[i - 1] == s2[j - 1]:
                            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
                        else:
                            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

                print(dp[-1][-1])
    except:
        break