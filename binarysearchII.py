def binarySearch(A, l, r, x):
    mid = (l+r)//2
    print (l, r, mid)
    if r == l:
        if A[mid] == x:
            print ("Hi here")
            return 0
        else: 
            return -1
    else:
        if A[mid] == x:
            print ("Hi there")
            return 0
        else:
            if A[mid] > x: 
                return binarySearch(A, l, mid-1, x)
            else:
                return binarySearch(A, mid, r, x)




if __name__ == "__main__":
    A = [2, 5, 7, 8, 12, 14, 20, 27]
    val = 19
    C = binarySearch(A, 0, len(A)-1, val)
    print(C)