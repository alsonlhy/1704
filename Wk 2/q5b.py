import random

n = random.randint(1, int(input("Provide an integer: ")))

print(n)


#OR

n = int(input("Provide an integer: "))
print (random.randint(1,n))

#randrange(a,b) --> a <= N < b
#randint(a,b) --> a <= N <= b

