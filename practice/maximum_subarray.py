# Maximum Sub Array
# https://practice.geeksforgeeks.org/problems/maximum-sub-array5443/1

def findSubarray(a, n):
    currentSum = 0
    currentStartPoint = 0
    currentLength = 0
    maxSum = 0
    finalStartPoint = 0
    finalEndPoint = 0
    maxLength = 0

    for i in range(0, n):
        if a[i] < 0:
            currentStartPoint = i + 1
            currentSum = 0

        else:
            currentLength = i - currentStartPoint + 1
            currentSum = currentSum + a[i]

        if currentSum == maxSum:
            if currentLength > maxLength:
                finalStartPoint = currentStartPoint
                finalEndPoint = i
                maxLength = currentLength

        if currentSum > maxSum:
            maxSum = currentSum
            finalStartPoint = currentStartPoint
            finalEndPoint = i
            maxLength = currentLength

        # print("i: ", i, "arr[i]: ", arr[i], "currentSum: ", currentSum, "max sum: ", maxSum, "currentStartPoint: ",
        #       finalStartPoint, "startPoint: ", finalStartPoint, "currentEndPoint: ", currentEndPoint, "endPoint: ",
        #       finalEndPoint, "currentLength: ", currentLength, "maxLength: ", maxLength, )

    if maxLength == 0:
        return [-1]

    else:
        return a[slice(finalStartPoint, finalEndPoint + 1)]


# arr = [2, 2, 2, -5, 1, 2, 3]
# print(findSubarray(arr, len(arr)))
