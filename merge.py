
def merge(A, l, m, r):
    n1 = m-l+1
    n2 = r-m-1
    

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = A[i]

    for i in range(n2):
        R[i] = A[m+1+i]

    print (L, R)
    i,j=0,0
    n=l
    while i<n1 and j<n2:
        if L[i] < R[j]:
            A[n] = L[i]
            i += 1
        else:
            A[n] = R[j]
            j += 1
        n += 1


    if i < n1:
        while i < n1:
            A[n] = L[i]
            i += 1
    else:
        while j < n2:
            A[n] = R[j]
            j += 1

        

if __name__ == "__main__":
    A = [2,1,3]
    merge(A, 0, 0, len(A))
    print(A)
