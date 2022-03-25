# Find Transition Point
# https://practice.geeksforgeeks.org/problems/find-transition-point-1587115620/1

def transitionPoint(arr, n):
    start = 0
    end = n - 1
    mid = (start + end) // 2

    def finder(start, end, mid):
        if end - start == 0:
            if arr[end] == 1:
                return end

            else:
                return -1

        elif end - start == 1:
            if arr[start] == 1:
                return start

            elif arr[end] == 1:
                return end

            else:
                return -1

        elif arr[mid] == 0:
            start = mid
            mid = (start + end) // 2

        elif arr[mid] == 1:
            end = mid
            mid = (start + end) // 2

        return finder(start, end, mid)

    return finder(start, end, mid)
