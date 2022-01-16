while True:
    try:
        hex_string = input()
        num_string = hex_string[2:]
        print(int(num_string, 7))
    except:
        break