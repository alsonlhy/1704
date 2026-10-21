
### Q4: Reset PIN


def is_valid_pin(new_pin, confirm_pin):

    if new_pin != confirm_pin:

        return False

    if len(new_pin) != 6 and len(confirm_pin) != 6:

        return False

    if not new_pin.isdigit():

        return False

    return True

def print_errors(error_msg):

# write list of error messages
# write error_esg = []
# check then use .append


new_pin = input("Enter your new PIN: ")
confirm_pin = input("Confirm your new PIN: ")
error_msg = is_valid_pin(new_pin, confirm_pin)


while not (is_valid_pin(new_pin, confirm_pin)):

    print("Sorry! There is an error!")
    print()
    new_pin = (input("Enter your new PIN: "))
    confirm_pin = (input("Confirm your new PIN: "))

print("Thanks! Your new PIN has been set!") 


        