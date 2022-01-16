while True:
    try:
        n = int(input())
        nums = []
        for i in range(n):
            num = int(input())
            nums.append(num)
        new_nums = list(set(nums))
        new_nums.sort()
        for num in new_nums:
            print(num)
    except:
        break