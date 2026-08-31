# lab2_Q6
# ################################################################################
# The following code is given to you.

def compute_phone_bill(base, data_limit, amount_data=0.0, num_extra_sms=0, num_minutes_extra_calls=0):
    return base + max(0.0, (amount_data - data_limit * 1024)) * 4.5 + num_extra_sms * 0.05 + num_minutes_extra_calls * 0.15

# ################################################################################
# You can verify your answers to Q6 by running the function calls below.

print(compute_phone_bill(35.5, 2, 800))
print(compute_phone_bill(35.5, 3))
print(compute_phone_bill(22.5,0))
print(compute_phone_bill(35.5, data_limit=2, amount_data=800))
print(compute_phone_bill(base=35.5, data_limit=2, amount_data=800))
print(compute_phone_bill(data_limit=2, amount_data=800, base=20))
print(compute_phone_bill(35.5, amount_data=800, data_limit=2))
print(compute_phone_bill(0.0,amount_data=800, data_limit=2))
print(compute_phone_bill(32, 2, 800))
print(compute_phone_bill(35.5, 2, 2050))
print(compute_phone_bill(35.5, 2, 1900, 10, 20))
print(compute_phone_bill(35.5, 2, num_minutes_extra_calls=100))
print(compute_phone_bill(35.5, 2, num_minutes_extra_calls=100, num_extra_sms=100))

#ln 11: base 35.5, limit 2, amt 800 --> 35.5 + max(0.0(800-2 * 1024))*4.5 + 0 + 0 --> 35.5
#ln 12: ans 35.5 too
#ln 13: ans 22.5
#ln 14: ans 35.5, same arguments as ln 11
#ln 15: ans 35.5
#ln 16: ans 20.0
#ln 17: ans 35.5
#ln 18: ans 0.0
#ln 19: ans 32.0
#ln 20: ans 44.5
#ln 21: ans 35.5 + 0 + 0.5 + 3 --> 39.0
#ln 22: ans 50.5
#ln 23: ans 55.5