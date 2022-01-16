num = int(input())
words = []
for i in range(num):
    words.append(input())
words.sort()
for word in words:
    print(word)