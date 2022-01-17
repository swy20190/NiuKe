while True:
    try:
        m_1 = []
        m_2 = []
        x = int(input())
        y = int(input())
        z = int(input())
        for i in range(x):
            m_1.append(list(map(int, input().strip().split())))
        for i in range(y):
            m_2.append(list(map(int, input().strip().split())))

        for i in range(x):
            for j in range(z):
                value = 0
                for p in range(y):
                    value += m_1[i][p] * m_2[p][j]
                print(value, end=' ')
            print("\n", end='')


    except:
        break