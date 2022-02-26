# Searching an element in a sorted array (Ternary Search)
# https://practice.geeksforgeeks.org/problems/3d27d4683c121c1f152ee8f41279255dc4430cf6/1

def ternarySearch(arr, n, k):
    def search(arr, start, end, k):
        firstPoint = (end - start) // 3 + start
        secondPoint = (2 * (end - start) // 3) + start

        if (end - start) < 2:
            if arr[start] == k or arr[end] == k:
                return 1
            else:
                return -1

        else:
            if k <= arr[firstPoint]:
                start = start
                end = firstPoint

            elif k >= arr[secondPoint]:
                start = secondPoint
                end = end

            else:
                start = firstPoint
                end = secondPoint

            return search(arr, start, end, k)

    initialStart = 0
    initialEnd = n - 1

    return search(arr, initialStart, initialEnd, k)
