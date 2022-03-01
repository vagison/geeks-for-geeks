# Wave Array
# https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1

def convertToWave(arr, n):
    for i in range(0, n - 1, 2):
        tmp = arr[i + 1]
        arr[i + 1] = arr[i]
        arr[i] = tmp

    return arr
