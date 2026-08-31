# Write a function print_square(symbol, size)

def print_square(symbol, size):
    length = symbol * size

    middle_row = symbol + (" " * (size-2)) + symbol
    middle_section = middle_row * (size-2)

    print(f"{length}\n{middle_section}\n{length}")



print_square('*', 5)

num = 5
if num > 2:
    print(num)
    num = num - 1
print(num)