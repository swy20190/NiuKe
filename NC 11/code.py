n, v = list(map(int, input().split()))
v_list = []
w_list = []
for i in range(n):
    vi, wi = list(map(int, input().split()))
    v_list.append(vi)
    w_list.append(wi)
dp1 = [0] * (v + 1)
dp2 = [float("-inf")] * (v + 1)
dp2[0] = 0
for i in range(n):
    for j in range(v, v_list[i] - 1, -1):
        dp1[j] = max(dp1[j], dp1[j - v_list[i]] + w_list[i])
        dp2[j] = max(dp2[j], dp2[j - v_list[i]] + w_list[i])

print(dp1[v])
if dp2[v] != float("-inf"):
    print(dp2[v])
else:
    print(0)