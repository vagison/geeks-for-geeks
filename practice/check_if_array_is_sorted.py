# Check if array is sorted
# https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

def arraySortedOrNot(arr, n):
    answer = True

    for i in range(0, n - 1):
        if arr[i + 1] < arr[i]:
            answer = False
            break

    return answer
