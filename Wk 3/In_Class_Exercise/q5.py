
# not True or (3 >= 3 or 9 < 4) and False
# False or True and False
# False or False
# False


# not True or 3 >= 3 or 9 < 4 and False
# not True or True or False and False
# False or True or False and False
# True or False
# True

# False == (False or not True) or not (2 * 4 % 3 == 1)
# False == (False) or not (True)
# False == (False) or False
# False == False
# True

print(False == (False or not True) or not (2 * 4 % 3 == 1))