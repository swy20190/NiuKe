def solve(arr, target):
    if len(arr)==1:
        return target==arr[0]
    else:
        for i in range(len(arr)):
            new_arr = arr[0:i]+arr[i+1:]
            if solve(new_arr, target+arr[i]) or solve(new_arr, target-arr[i]) or solve(new_arr, target*arr[i]) or solve(new_arr, target/arr[i]):
                return True
        return False

while True:
    try:
        arr_four = list(map(int, input().split()))
        if solve(arr_four, 24):
            print("true")
        else:
            print("false")
    except:
        break