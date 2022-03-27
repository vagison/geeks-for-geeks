# Remove duplicate elements from sorted Array
# https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1

def remove_duplicate(A, N):
    index = N - 1

    while index > 0:
        if(A[index] == A[index-1]):
            A.pop(index)

        index -= 1

    return len(A)
