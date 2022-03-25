# Rotate Array
# https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1
# Solved with the help of the auxiliary space of O(d)

def rotateArr(A, D, N):
    tmp = A[0:D]

    for i in range(0, N-D):
        A[i] = A[i+D]

    for x in range(N-D, N):
        A[x] = tmp[x-(N-D)]
