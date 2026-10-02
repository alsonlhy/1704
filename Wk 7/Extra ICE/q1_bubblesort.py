def bubble_sort(a):

    n = len(a)

    for i in range(n-1):

        for r in range(n-1-i):

            if a[r] > a[r+1]:
                a[r], a[r+1] = a[r+1], a[r]

    return a

a = [2,5,6,3,9,1,8,4]

print(bubble_sort(a))