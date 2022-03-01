# Segregate 0s and 1s
# https://practice.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1/

def segregate0and1(arr, n):
    sum = 0

    for i in range(0, n):
        if arr[i] == 1:
            sum += 1

    for j in range(0, (n-sum)):
        arr[j] = 0

    for k in range((n-sum), n):
        arr[k] = 1
