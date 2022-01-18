while True:
    try:
        n = int(input())
        raw = list(map(int, input().split()))
        cnt = 0
        pos_list = []
        for num in raw:
            if num < 0:
                cnt += 1
            elif num > 0:
                pos_list.append(num)
        print(cnt, end=' ')
        print(round(sum(pos_list) / len(pos_list), 1))

    except:
        break