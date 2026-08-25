# ################################################################################
# Implement the function below:
def compute_geometric_mean(x, y, z):
    """
    This function returns the geometric mean of the three numbers x, y and z.
    """
    # Write your code here:
    return ((x * y * z)**(1/3))




# ################################################################################    
# The code below is to test your implementation above.
# DO NOT MODIFY THE CODE BELOW!

print("The geometric mean of 2, 4 and 6 is:", compute_geometric_mean(2, 4, 6))

num4 = float(input("First number: "))
num5 = float(input("Second number: "))
num6 = float(input("Third number: "))

geometric_mean = compute_geometric_mean(num4, num5, num6)
print(f"The geometric mean of {num4}, {num5} and {num6} is : {geometric_mean}")