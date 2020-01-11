def partition(A, l, h):
    pivot = A[l]
    i, j = l, h
    while i < j:
        while (A[i] <= pivot): 
            i += 1
            if i > h: 
                break
        while (A[j] > pivot):
            j -= 1
            if j < l:
                break
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]
    return j

    
def quicksort(B, l, h):
    if l < h: 
        j = partition (B, l, h)
        quicksort(B, l, j)
        quicksort(B, j+1, h)


if __name__ == "__main__":      
    A = [10, 5, 2, 12, 1, 8, 18, 11, 7]
    l = 0
    r = len(A) 
    print ("Start:")
    print(A)
    quicksort(A, l, r-1)
    print("Final:")
    print(A)
