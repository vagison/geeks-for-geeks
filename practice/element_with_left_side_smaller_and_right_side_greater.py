# Element with left side smaller and right side greater
# https://practice.geeksforgeeks.org/problems/unsorted-array4925/1

def findElement(arr, n):
    m = arr[0]
    pivot = n
    lp = m

    for i in range(1, n):
        if arr[i] >= m:
            m = arr[i]

            if i < pivot and i != (n-1):
                pivot = i
                lp = arr[pivot]

        elif arr[i] < lp:
            pivot = n

    if pivot == n:
        return -1

    else:
        return arr[pivot]
