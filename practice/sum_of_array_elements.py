# Sum of Array Elements
# https://practice.geeksforgeeks.org/problems/sum-of-array-elements2502/1

def sumElement(arr, n):
    sum = 0

    for i in range(0, n):
        sum += arr[i]

    return sum
