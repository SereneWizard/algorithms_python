def partition(A, l, h):
    pivot = A[l]
    i, j = l+1, h
    while i < j:
        while (A[i] < pivot): 
            i += 1
        while (A[j] > pivot):
            j -= 1
        if i < j:
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
    temp = A[j]
    A[j] = pivot
    A[l] = temp
    print(A)
    return j

    

def quicksort(B, l, h):
    j = partition (B, l, h)
    print(l,h,j)
    quicksort(B, l, j-1)
    quicksort(B, j+1, h)
    print(j)




if __name__ == "__main__":      
    A = [10, 5, 2, 12, 1, 8, 18, 11, 7]
    l = 0
    r = len(A) 
    print ("Start:")
    print(A)
    quicksort(A, l, r-1)
    print("Final:")
    print(A)
