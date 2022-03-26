# First Repeating Element
# https://practice.geeksforgeeks.org/problems/first-repeating-element4018/1

def firstRepeated(arr, n):
    hashMap = {}

    for item in arr:
        if not (item in hashMap):
            hashMap[item] = 1
        else:
            hashMap[item] += 1

    searchedElement = -1

    for index in range(0, n):
        if hashMap[arr[index]] > 1:
            searchedElement = index + 1
            break

    return searchedElement
