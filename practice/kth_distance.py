# Kth distance
# https://practice.geeksforgeeks.org/problems/kth-distance3757/1

def checkDuplicatesWithinK(arr, n, k):
    hashMap = {}
    answer = False

    for numberIndex in range(0, n):
        if not (arr[numberIndex] in hashMap):
            hashMap[arr[numberIndex]] = [numberIndex, numberIndex, 0]

        else:
            hashMap[arr[numberIndex]][0] = hashMap[arr[numberIndex]][1]
            hashMap[arr[numberIndex]][1] = numberIndex

            distance = hashMap[arr[numberIndex]][1] - \
                hashMap[arr[numberIndex]][0]
            if distance <= k:
                hashMap[arr[numberIndex]][2] = distance

    for number in hashMap:
        if hashMap[number][2] != 0:
            answer = True
            break

    return answer
