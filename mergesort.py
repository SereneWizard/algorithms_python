from merge import merge



def mergesort(A, l , r):
    if l < r:
        m = (l+r)/2
        mergesort(A, l, m)
        mergesort(A, m, h)
        merge(A, l, m, r)


if __name__ == "__main__":
    A = [5, 10, 2, 12, 7, 15, 6, 3]
    l = 0
    r = len(A) -1 
    C = mergesort(A, l, r)
    print (C)