# Minimum steps to make product equal to one
# https://practice.geeksforgeeks.org/problems/minimum-steps-to-make-product-equal-to-one/1


def makeProductOne(arr, N):
    negativesCount = 0
    isZero = False
    stepCounter = 0

    for i in range(0, N):
        if arr[i] < 0:
            negativesCount += 1

        if arr[i] == 0:
            isZero = True

        stepCounter += abs(abs(arr[i]) - 1)

    if negativesCount % 2 == 1:
        if not isZero:
            stepCounter += 2

    return stepCounter
