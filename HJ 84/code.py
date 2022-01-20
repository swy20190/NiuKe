while True:
    try:
        string = input()
        answer = 0
        for c in string:
            if ord(c)>=ord('A') and ord(c)<=ord('Z'):
                answer += 1
        print(answer)
    except:
        break