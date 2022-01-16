input_string = input()
char_list = []
n = len(input_string)
for i in range(n):
    num_i = int(input_string[n-1-i])
    if not num_i in char_list:
        char_list.append(num_i)
output_string = ""
for i in char_list:
    output_string += str(i)
print(output_string)