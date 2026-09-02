# Write a function print_square(symbol, size)

def print_square(symbol, size):
    length = symbol * size

    middle_row = symbol + (" " * (size-2)) + symbol
    middle_section = middle_row * (size-2)

    print(f"{length}\n{middle_section}\n{length}")



print_square('*', 5)