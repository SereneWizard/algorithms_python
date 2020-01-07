A = [5, 10, 2, 12, 7, 15, 6, 3]

n = len(A)


for i in range(n):
    smallest = A[i]
    smallestindex = i
    for j in range(i, n):
        if A[j] < smallest:
            smallest = A[j]
            smallestindex = j
    A[i], A[smallestindex] = A[smallestindex], A[i]
    print(A)



print ("Hello")