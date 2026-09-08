def print_message_with_separators(msg, sep):
    for i in range(0, len(msg)-1):
        ch = msg[i]
        print(ch + sep, end="")
    print(msg[-1])

print_message_with_separators("Python", "/")