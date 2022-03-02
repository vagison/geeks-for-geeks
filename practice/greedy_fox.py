# Greedy Fox
# https://practice.geeksforgeeks.org/problems/greedy-fox1555/0


def largestSum(arr, N):
    currentAmount = arr[0]
    maximumMoney = currentAmount

    for i in range(1, N):
        if arr[i] > arr[i - 1]:
            currentAmount += arr[i]

        else:
            currentAmount = arr[i]

        if currentAmount > maximumMoney:
            maximumMoney = currentAmount

    return maximumMoney
