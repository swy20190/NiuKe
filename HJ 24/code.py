import bisect


def dp_list(hs):
    arr = [hs[0]]
    dp = [1]
    for i in range(1, len(hs)):
        if hs[i] > arr[-1]:
            arr.append(hs[i])
            dp.append(len(arr))
        else:
            idx = bisect.bisect_left(arr, hs[i])
            arr[idx] = hs[i]
            dp.append(idx + 1)
    return dp


while True:
    try:
        n = int(input())

        heights = list(map(int, input().split()))

        heights_r = heights[::-1]

        dp = dp_list(heights)

        dp_r = dp_list(heights_r)
        answer = 0
        for i in range(len(dp)):
            answer = max(answer, dp[i] + dp_r[len(dp) - i - 1])
        print(str(n - answer + 1))
    except:
        break