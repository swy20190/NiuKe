while True:
    try:
        string = input()
        eng_cnt = 0
        space_cnt = 0
        num_cnt = 0
        other_cnt = 0
        for ch in string:
            if (ord(ch)-ord('a')<26 and ord(ch)-ord('a')>=0) or (ord(ch)-ord('A')>=0 and ord(ch)-ord('A')<26):
                eng_cnt += 1
            elif ch==' ':
                space_cnt += 1
            elif ord(ch)-ord('0')<10 and ord(ch)-ord('0')>=0:
                num_cnt += 1
            else:
                other_cnt += 1
        print(eng_cnt)
        print(space_cnt)
        print(num_cnt)
        print(other_cnt)
    except:
        break