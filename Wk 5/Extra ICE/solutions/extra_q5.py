# Name:
# Email ID:


def caesar_cipher(plain_text, n):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    s_to_return = ''
    for ch in plain_text:
        if ch in lowercase:
            index = lowercase.find(ch)
            # % 26 makes the alphabet "wrap around" from z back to a
            s_to_return += lowercase[(index + n) % 26]
        elif ch in uppercase:
            index = uppercase.find(ch)
            s_to_return += uppercase[(index + n) % 26]
        else:
            # punctuation, digits and whitespace are left unchanged
            s_to_return += ch

    return s_to_return