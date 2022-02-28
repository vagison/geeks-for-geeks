# Find duplicates in an array
# https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1

def duplicates(arr, n):
    verifyingArray = []
    resultingArray = []

    for i in range(0, n):
        verifyingArray.append(0)

    for i in range(0, n):
        verifyingArray[arr[i]] += 1

    for i in range(0, n):
        if verifyingArray[i] > 1:
            resultingArray.append(i)

    if len(resultingArray) < 1:
        return -1

    return resultingArray
