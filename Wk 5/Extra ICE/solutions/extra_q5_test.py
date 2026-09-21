from extra_q5 import caesar_cipher

# Expected output:
#     efgh bcd
#     Khoor, Zruog!
#     (an empty line)
#     abcd xyz
#     Hello, World!

print(caesar_cipher("abcd xyz", 4))
print(caesar_cipher("Hello, World!", 3))
print(caesar_cipher("", 5))

# encrypting by n and then by -n should give back the original text
print(caesar_cipher(caesar_cipher("abcd xyz", 4), -4))
print(caesar_cipher(caesar_cipher("Hello, World!", 3), -3))