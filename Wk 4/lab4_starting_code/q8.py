## Q8
# ################################################################################
# The function below is for you to implement! 
def display_fibonacci(n):
    """
    This function takes in an integer n (greater or equal to 3). It prints out the 
    first n Fibonacci numbers, starting from 1. The function doesn’t return anything.
    """
    # Modify the code below to print the first n Fibonacci numbers

    a = 1
    b = 1

    print(b, end=" ")

    for i in range(n-2):

        i = a + b
        print(i, end=" ")

        a = b
        b = i 




(display_fibonacci(10))

