def merge(A, l, m, r):
    print (l, m, r)
    print ("Here now")
    L = A[l:m+1]
    R = A[m+1:r+1]
    n1 = len(L)
    n2 = len(R)
    print(n1, n2)
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
    else:
        while j < n2:
            A[n] = R[j]
            j += 1



def mergesort(A, l , r):
    m = (l+(r-1))//2
    if l < r:
        print("firstside")
        mergesort(A, l, m)
        print("secondside")
        mergesort(A, m+1, r)
        print("mergeside")
        merge(A, l, m, r)



if __name__ == "__main__":      
    A = [10, 5, 2, 12, 1, 3, 18, 9]
    l = 0
    r = len(A) 
    mergesort(A, l, r-1)
    print(A)
