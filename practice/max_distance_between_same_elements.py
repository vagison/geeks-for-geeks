# Max distance between same elements
# https://practice.geeksforgeeks.org/problems/max-distance-between-same-elements/1

def maxDistance(arr, n):
    hashMap = {}

    for index in range(0, n):
        if not (arr[index] in hashMap):
            hashMap[arr[index]] = [index]

        elif (len(hashMap[arr[index]]) == 1):
            hashMap[arr[index]].append(index)

        else:
            hashMap[arr[index]][1] = index

    maxDistanceValue = 0

    for element in hashMap:
        if len(hashMap[element]) > 1:
            delta = hashMap[element][1] - hashMap[element][0]

            if (delta > maxDistanceValue):
                maxDistanceValue = delta

    return maxDistanceValue
