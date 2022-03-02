# Bitonic Point
# https://practice.geeksforgeeks.org/problems/maximum-value-in-a-bitonic-array3001/1

def findMaximum(arr, n):
    startingPoint = 0
    midPoint = (n - 1) // 2
    endPoint = n - 1

    while endPoint - midPoint > 1:
        if arr[midPoint] < arr[midPoint + 1]:
            startingPoint = midPoint
            midPoint = (startingPoint + endPoint) // 2

        else:
            endPoint = midPoint
            midPoint = endPoint // 2

    if arr[midPoint] > arr[endPoint]:
        return arr[midPoint]

    return arr[endPoint]
