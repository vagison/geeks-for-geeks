# Union of Two Sorted Arrays 
# https://practice.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1

def mergeArrays(a, b, n, m):
    result = []
    totalLength = n + m
    indexA = 0
    indexB = 0

    if a[indexA] <= b[indexB]:
        result.append(a[indexA])
        indexA += 1
    else:
        result.append(b[indexB])
        indexB += 1

    index = 1

    while index < totalLength:
        while indexA < n and indexB < m:
            if a[indexA] <= b[indexB]:
                if result[len(result) - 1] < a[indexA]:
                    result.append(a[indexA])
                indexA += 1

            else:
                if result[len(result) - 1] < b[indexB]:
                    result.append((b[indexB]))
                indexB += 1

            index += 1

        while indexA < n:
            if result[len(result) - 1] < a[indexA]:
                result.append(a[indexA])
            indexA += 1
            index += 1

        while indexB < m:
            if result[len(result) - 1] < b[indexB]:
                result.append(b[indexB])
            indexB += 1
            index += 1

    return result
