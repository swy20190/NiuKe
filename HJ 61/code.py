def place(m, n):
    if m == 0:
        return 1
    if m == 1:
        return 1
    if n == 1:
        return 1

    if m >= n:
        return place(m - n, n) + place(m, n - 1)
    else:
        return place(m, m)


while True:
    try:
        m, n = list(map(int, input().split()))
        print(place(m, n))
    except:
        break