# The Optimal Selection
# https://practice.geeksforgeeks.org/problems/the-optimal-selection5413/1

def selection(arr, n):
    arr.sort()

    sum = 0
    for i in range(0, n):
        sum = sum + arr[i]*i

    return sum
