def exist_sum(arr, target):
    if target==0:
        return True
    if len(arr)==1:
        return arr[0] == target
    else:
        for i in range(len(arr)):
            new_arr = arr[:i]+arr[i+1:]
            if exist_sum(new_arr, target-arr[i]):
                return True
        return False

while True:
    try:
        n = int(input())
        nums = list(map(int, input().strip().split()))
        list3 = []
        list5 = []
        pure_nums = []
        nums_sum = 0
        for num in nums:
            nums_sum +=num
            if num%5 == 0:
                list5.append(num)
            elif num%3 == 0:
                list3.append(num)
            else:
                pure_nums.append(num)
        if nums_sum%2 != 0:
            print("false")
            
        else:
            if exist_sum(pure_nums, nums_sum/2-sum(list5)):
                print("true")
            else:
                print("false")
    except:
        break