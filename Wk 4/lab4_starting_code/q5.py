def pad_message(msg, width):

    if len(msg) < width:
        space = width - len(msg)
        return " " * space + msg

    else:
        return msg[:width]


            

print(pad_message("COR-IS1704 Lab 4", 20))
print(pad_message("COR-IS1704 Lab 4", 8))
print(pad_message("hello", 20))
print(pad_message("python programming", 20))
print(pad_message("Hello World! I enjoy programming in Python.", 20))