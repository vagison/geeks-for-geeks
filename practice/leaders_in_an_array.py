# Leaders in an array
# https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

def leaders(A, N):
    storage = []
    x = N - 1

    max = A[x]

    while(x >= 0):
        if A[x] >= max:
            storage.append(A[x])
            max = A[x]
        x = x - 1

    storage.reverse()

    return storage
