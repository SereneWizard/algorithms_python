def binarySearch(searchList, value):
    print(searchList)
    n = len(searchList)
    mid = n//2
    print(mid)
    if mid != 0:
        print (searchList[mid])
        if value == searchList[mid]:
            print ("hi there")
            return 0
        else:
            if value < searchList[mid]:
                binarySearch(searchList[0:mid], value)
            else:
                binarySearch(searchList[mid:n], value)
    else:
        if value == searchList[mid]:
            return 0
        else:
            return -1


if __name__ == "__main__":
    A = [2, 5, 7, 8, 12, 14, 20, 27]
    val = 14
    C = binarySearch(A, val)
    print(C)