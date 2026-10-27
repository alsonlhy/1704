## Q2 Prime Numbers
# write your code below

import sympy

def create_prime_dict(int_list):

    new_dict = {}

    for num in int_list:

        if sympy.isprime(num):
            new_dict[num] = True

        else:
            new_dict[num] = False

    return new_dict