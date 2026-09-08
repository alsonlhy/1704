msg = input("Enter a word: ")

if msg == msg[::-1]:
    print(f"{msg} is a palindrome")

else:
    print(f"{msg} is NOT a palindrome")