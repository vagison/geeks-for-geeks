# Immediate Smaller Element
# https://practice.geeksforgeeks.org/problems/immediate-smaller-element1142/1

def immediateSmaller(arr, n):
    # code here
    for i in range(0, n):
        if(i + 1 > n - 1):
            arr[i] = -1
            break
        if arr[i] > arr[i + 1]:
            arr[i] = arr[i + 1]
        else:
            arr[i] = -1
