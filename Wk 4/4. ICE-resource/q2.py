def display_numbers(m,n):
    for i in range(m,n+1):
        if i % 5 == 0 and i % 3 == 0:
            i = "#"
        
        elif i % 3 == 0:
            i = "-"

        elif i % 5 == 0:
            i = "*"


        print(i, end=" ")

display_numbers(4,16)