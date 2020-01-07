A = [5, 10, 2, 12, 7, 15, 6, 3]

n = len(A)

for i in range(n, 1, -1):
    for j in range(1,i):
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]

print (A)
print ("Hello")