# K-th missing element
# https://practice.geeksforgeeks.org/problems/k-th-missing-element3635/1

def kthMissingElement(arr, n, k):
    currentIndex = 0
    expectedNextItem = arr[currentIndex] + 1
    numberOfMissingItems = 0

    while numberOfMissingItems < k and currentIndex < n - 1:
        if arr[currentIndex + 1] > expectedNextItem:
            numberOfMissingItems += 1
            expectedNextItem += 1

        else:
            currentIndex += 1
            expectedNextItem = arr[currentIndex] + 1

    if numberOfMissingItems == k:
        return expectedNextItem - 1

    return -1
