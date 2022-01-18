import math
a, b = list(map(int, input().split()))
answer = a*b/math.gcd(a, b)
print(int(answer))