# Missing number in shuffled array
# https://practice.geeksforgeeks.org/problems/missing-number-in-shuffled-array0938/1

def findMissing(a, b, n):
    missingNumber = a[0]

    for i in range(1, n):
        missingNumber = missingNumber ^ a[i]

    for j in range(0, n-1):
        missingNumber = missingNumber ^ b[j]

    return missingNumber
