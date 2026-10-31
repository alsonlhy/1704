## Q2 Prime Numbers
# write your code below

# import sympy

# def create_prime_dict(int_list):

#     new_dict = {}

#     for num in int_list:

#         if sympy.isprime(num):
#             new_dict[num] = True

#         else:
#             new_dict[num] = False

#     return new_dict

def create_prime_dict(num_list):
    prime_dict = {}

    for num in num_list:
        is_prime = True


        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        prime_dict[num] = is_prime

    return prime_dict