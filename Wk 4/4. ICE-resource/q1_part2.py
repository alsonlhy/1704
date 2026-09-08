msg = input("Enter a message: ")

for i in range(0, len(msg)-1):
    ch = msg[i]
    print(ch + "-", end="")

print(msg[-1])

# OR

# for ch in msg[0:len(msg)-1]:
    # print(ch + '-', end="")


# OR

message = input('enter a message: ')
str_to_print = ""

for ch in message:
    str_to_print += ch + '-'

print(str_to_print[0:len(str_to_print)-1])


