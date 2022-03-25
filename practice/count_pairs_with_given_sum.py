# Count pairs with given sum
# https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

def getPairsCount(arr, n, k):
    hashMap = {}

    for item in arr:
        if not (item in hashMap):
            hashMap[item] = 1
        else:
            hashMap[item] += 1

    counter = 0

    for addend in hashMap:
        if k - addend in hashMap:
            if k == 2 * addend:
                counter += hashMap[addend] * (hashMap[addend] - 1)
            else:
                counter += hashMap[addend] * hashMap[k - addend]

    return counter // 2
