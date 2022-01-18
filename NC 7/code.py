n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
sum_list = [0] * (n + 1)
for i in range(m):
    l, r, k = list(map(int, input().split()))
    sum_list[l - 1] += k

    sum_list[r] -= k
for i in range(1, n):
    sum_list[i] += sum_list[i - 1]
for i in range(n):
    print(sum_list[i] + arr[i], end=' ')