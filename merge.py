
def merge (A, B):
    na = len(A)
    nb = len(B)
    n = na + nb

    C = [None]*n
    ha = 0
    hb = 0
    i = 0
    while ha < na and hb < nb:
        if A[ha] <= B[hb]:
            C[i] = A[ha]
            ha += 1
        else:
            C[i] = B[hb]
            hb += 1
        i += 1

    if ha > na:
        while hb < nb: 
            C[i] = B[hb]
            hb += 1
            i += 1
    else: 
        while ha < na:
            C[i] = A[ha]
            ha += 1
            i += 1
    return C

if __name__ == "__main__":
    A = [2, 7, 8, 12, 17, 20]
    B = [3, 4, 9, 11, 15]
    C = merge(A, B)
    print(C)