def compute_sum(m,n):

    num_sum = 0 
    for i in range(m,n+1):
        num_sum += i

    return num_sum

my_sum = compute_sum(4, 10)
print("The sum is " + str(my_sum))