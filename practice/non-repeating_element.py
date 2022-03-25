# Non-Repeating Element
# https://practice.geeksforgeeks.org/problems/non-repeating-element3958/1/

def firstNonRepeating(arr, n):
    hashMap = {}

    for i in range(0, n):
        if not (arr[i] in hashMap):
            hashMap[arr[i]] = 1
        else:
            hashMap[arr[i]] += 1

    searchedElement = 0

    for i in range(0, n):
        if hashMap[arr[i]] == 1:
            searchedElement = arr[i]
            break

    return searchedElement
