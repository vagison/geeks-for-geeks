# Missing number in array
# https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1

def missingNumber(array, n):
    # code here
    sum = int((1 + n)/2*n)

    for i in range(0, n - 1):
        sum = sum - array[i]

    return sum
