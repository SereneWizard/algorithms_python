
def partitioning(A, l, h):
    pivot = A[l]
    i = l
    j = h-1
    while (i < j): 
        while (A[i] < pivot):
            i += 1
        while (A[j] > pivot):
            j -= 1
        print(i,j)
        if (i < j):
            A[i], A[j] = A[j], A[i]
        
    A[l], A[j] = A[j], A[l]
    return j
        

def quicksort(B, l, h):
    if (l < h):
        j = partitioning(B, l, h)
        print(B)
        quicksort(B, l,j)
        quicksort(B, j+1, h)

def interface(B):
    n = len(B)
    l = 0
    h = n
    quicksort(B, l, h)

if __name__ == "__main__":
    A = [5, 10, 2, 12, 7, 15, 6, 3]
    interface(A)
    print("Hello")
    print (A)