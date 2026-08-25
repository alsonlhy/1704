# ################################################################################
# The following code is given to you.
def compute_average(a, b, c):
    """ 
    This function returns the average of the three numbers a, b and c.
    """
    return (a + b + c)/3

# ################################################################################    
# Write your code below:

def compute_geometric_mean(x, y, z):

    return ((x * y * z)**(1/3))


num1 = float(input("First number: "))
num2 = float(input("Second number: "))
num3 = float(input("Third number: "))

average = compute_average(num1, num2, num3)
print(f"Average: {average:.2f}")

num4 = float(input("First number: "))
num5 = float(input("Second number: "))
num6 = float(input("Third number: "))

geometric_mean = compute_geometric_mean(num4, num5, num6)
print(f"The geometric mean of {num4}, {num5} and {num6} is : {geometric_mean}")