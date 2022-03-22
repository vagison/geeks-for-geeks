# Index Of an Extra Element
# https://practice.geeksforgeeks.org/problems/index-of-an-extra-element/1

def findExtra(a, b, n):
    start = 0
    end = n
    mid = (start + end) // 2

    def finder(start, end, mid):
        if mid == end or mid + 1 == n:
            if a[mid - 1] != b[mid - 1]:
                return mid - 1

            return mid

        elif a[mid] == b[mid]:
            start = mid + 1
            mid = (start + end) // 2

        else:
            end = mid
            mid = (start + end) // 2

        return finder(start, end, mid)

    return finder(start, end, mid)