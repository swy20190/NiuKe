while True:
    try:
        given_string = input()
        string_len = len(given_string)
        for i in range(int(string_len/8)):
            print(given_string[8*i:8*i+8])
        if string_len%8!=0:
            last_string = ""
            for i in range(8*int(string_len/8), string_len):
                last_string += given_string[i]
            for i in range(8-string_len%8):
                last_string += "0"
            print(last_string)
    except:
        break