import math
num = int(input())
for i in range(2, int(math.sqrt(num))+1):
    while num%i == 0:
        print(i, end=" ")
        num = num/i
if num>1:
    print(int(num))