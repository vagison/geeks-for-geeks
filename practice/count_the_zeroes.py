def countZeroes(arr, n):
    start = 0
    end = n - 1
    mid = (start + end) // 2

    def transitionPointFinder(start, end, mid):
        if end - start == 0:
            if arr[end] == 0:
                return end

            else:
                return -1

        elif end - start == 1:
            if arr[start] == 0:
                return start

            elif arr[end] == 0:
                return end

            else:
                return -1

        elif arr[mid] == 1:
            start = mid
            mid = (start + end) // 2

        elif arr[mid] == 0:
            end = mid
            mid = (start + end) // 2

        return transitionPointFinder(start, end, mid)

    transitionPoint = transitionPointFinder(start, end, mid)

    if transitionPoint == -1:
        return 0

    else:
        return n - transitionPoint
