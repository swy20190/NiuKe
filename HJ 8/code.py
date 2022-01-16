num = int(input())
dict = {}
for i in range(num):
    input_list = input().strip().split()
    index = int(input_list[0])
    value = int(input_list[1])
    if index in dict:
        dict[index] += value
    else:
        dict[index] = value
for i in sorted(dict):
    print(str(i) + " " + str(dict[i]))
