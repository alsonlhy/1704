msg = input("What's the original message? ")

encrypt = ""


for ch in msg:
    if ch == "a":
        encrypt += "e"

    elif ch == "e":
        encrypt += "i"

    elif ch == "i":
        encrypt += "o"

    elif ch == "o":
        encrypt += "u"

    elif ch == "u":
        encrypt += "a"

    else: 
        encrypt += ch

print(f"The encrypted message is: {encrypt}")

reverse = encrypt[::-1]
print(reverse)