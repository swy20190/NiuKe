input_string = input().strip()
buckets = []
for i in range(128):
    buckets.append(0)
for i in input_string:
    buckets[ord(i)] += 1

answer = 0
for i in range(128):
    if buckets[i] > 0:
        answer += 1
print(answer)