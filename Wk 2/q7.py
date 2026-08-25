# This line of code prompts the user for a system time.
input_str = input('Please enter the system time (in seconds): ')

################################################################################
# Complete the code below to get the correct numbers of days, hours, minutes and seconds.

num_days = 0
num_hours = 0
num_minutes = 0
num_seconds = 0

# Put your code below

tot_num_seconds = int(input_str)

NUM_SECONDS_PER_MINUTE = 60
NUM_SECOND_PER_HOUR = 60 * 60
NUM_SECOND_PER_DAY = 60 * 60 * 24

num_days = tot_num_seconds // NUM_SECOND_PER_DAY



################################################################################
# DO NOT MODIFY THE CODE BELOW!!!

# This line of code displays the results.
print('Based on this system time, ' + str(num_days) + ' days, ' + str(num_hours) + ' hours, ' + str(num_minutes) + ' minutes and ' + str(num_seconds) + ' seconds have passed since 1 January 1970 00:00:00 UT.')