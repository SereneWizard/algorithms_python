def merge(A, l, m, r):
    print (l, m, r)
    L = A[l:m+1]
    R = A[m+1:r+1]
    n1 = len(L)
    n2 = len(R)
    print(L, R)

    i = j = 0
    n = l
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
            n += 1

    else:
        while j < n2:
            A[n] = R[j]
            j += 1
            n += 1





if __name__ == "__main__":
    A = [1, 8, 7, 11, 18]
    merge(A, 0, 1, len(A))
    print("Final")
    print(A)
