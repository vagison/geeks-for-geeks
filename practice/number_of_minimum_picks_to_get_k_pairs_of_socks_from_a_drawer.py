# Number of minimum picks to get 'k' pairs of socks from a drawer
# https://practice.geeksforgeeks.org/problems/620fb6456d6515faddd77050dfbf2821d7a94b8a/1

def find_min(a, n, k):
    totalNumOfSocks = 0
    numOfPairs = 0

    for i in range(0, n):
        totalNumOfSocks += 1
        a[i] -= 1

    if numOfPairs < k:
        for i in range(0, n):
            totalNumOfPairsOfCurrentColor = a[i] // 2
            remainingSocksOfCurrentColor = a[i] % 2
            a[i] = remainingSocksOfCurrentColor

            if numOfPairs + totalNumOfPairsOfCurrentColor >= k:
                totalNumOfSocks = totalNumOfSocks + 2 * (k - numOfPairs)
                numOfPairs = k

            else:
                totalNumOfSocks = totalNumOfSocks + 2 * totalNumOfPairsOfCurrentColor
                numOfPairs += totalNumOfPairsOfCurrentColor

            if numOfPairs == k:
                totalNumOfSocks -= 1
                break

        for i in range(0, n):
            if numOfPairs == k:
                break

            if a[i] == 1:
                totalNumOfSocks += 1
                numOfPairs += 1

    if numOfPairs == k:
        return totalNumOfSocks

    else:
        return -1