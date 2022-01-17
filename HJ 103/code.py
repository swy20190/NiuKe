import bisect

def solve(n, arr):
    q = [arr[0]]
    for i in range(1, n):
        if arr[i]>q[-1]:
            q.append(arr[i])
        else:
            idx = bisect.bisect_left(q, arr[i])
            q[idx] = arr[i]
    return len(q)

while True:
    try:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(solve(n, arr))
    except:
        break