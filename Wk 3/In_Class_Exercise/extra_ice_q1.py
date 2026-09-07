def get_num_digits(n):
    if n < 10:
        return 1
    else:
        return 1 + get_num_digits(n // 10)

print(get_num_digits(146))