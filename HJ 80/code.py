while True:
    try:
        len1 = int(input())
        list1 = list(map(int, input().split()))
        len2 = int(input())
        list2 = list(map(int, input().split()))
        new_list = list(set(list1+list2))
        new_list.sort()
        for i in new_list:
            print(i, end='')
        print('')
    except:
        break