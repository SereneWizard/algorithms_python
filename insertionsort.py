A = [5, 10, 2, 12, 7, 15, 6, 3]

n = len(A)


for i in range(n):
    for j in range(i,0,-1):
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1], A[j]
        else:
            break

print (A)
print ("Hello")