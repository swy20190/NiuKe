while True:
    try:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        arr.sort()
        for i in range(k):
            print(arr[i], end=' ')
        print('')
    except:
        break
