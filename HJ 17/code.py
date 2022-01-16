operations = input().strip().split(";")
answer = [0, 0]
for operation in operations:

    if len(operation) == 0:
        continue
    ori = operation[0]

    try:
        distance = int(operation[1:])

        if ori == "A":
            answer[0] -= distance
        elif ori == "D":
            answer[0] += distance
        elif ori == "S":
            answer[1] -= distance
        elif ori == "W":
            answer[1] += distance
    except:
        pass
print(str(answer[0]) + "," + str(answer[1]))
