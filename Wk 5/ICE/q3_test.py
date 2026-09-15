from q3 import is_valid_username

print()
print('-' * 20)
print()

username_list = ['abcdefgh','abcdefghi','ab$cd','ab_cd','ab-cd','ab:cd','','ab cd','abcDef','abc8ef']
for username in username_list:
    print("The username '" + username +"' is valid : " + str(is_valid_username(username)))

print()
print('-' * 20)
print()
