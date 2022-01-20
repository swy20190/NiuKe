while True:
    try:
        a, b = list(map(int, input().split('/')))
        mothers = []
        while b % a != 0:
            c = int(b / a) + 1

            mothers.append(c)
            a = a * c - b
            b = b * c
        mothers.append(int(b / a))

        for i in range(len(mothers) - 1):
            print("1/" + str(mothers[i]), end='+')
        print("1/" + str(mothers[-1]))
    except:
        break