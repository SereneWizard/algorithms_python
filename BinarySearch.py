def binarySearch(A, l, r, x):
    mid = (l+r)//2
    print (l, r, mid)
    if r == l:
        if A[mid] == x:
            print ("Hi here")
            return mid
        else: 
            return -1
    else:
        if A[mid] == x:
            print ("Hi there")
            return mid
        else:
            if A[mid] > x: 
                return binarySearch(A, l, mid, x)
            else:
                return binarySearch(A, mid+1, r, x)




if __name__ == "__main__":
    A = [3, 5, 7, 8, 12, 14, 20, 27]
    val = 26
    C = binarySearch(A, 0, len(A)-1, val)
    if C != -1:
        print ("Value {} exists at index {}".format(val, C))
    else:
        print (C)