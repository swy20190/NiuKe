def related(number):
    return number%7==0 or str(number).count("7")>0

while True:
    try:
        n = int(input())
        answer = 0
        for i in range(1,n+1):
            if related(i):
                answer += 1
        print(answer)
    except:
        break