while True:
    try:
        n = int(input())
        app_list = input().strip().split()
        tick_num = int(input())
        tick_list = input().strip().split()
        invalid = 0
        tick_dict = {}
        for app in app_list:
            tick_dict[app] = 0
        for tick in tick_list:
            if tick in tick_dict:
                tick_dict[tick] += 1
            else:
                invalid += 1
        for app in app_list:
            print(app+" : "+str(tick_dict[app]))
        print("Invalid : "+str(invalid))
    except:
        break