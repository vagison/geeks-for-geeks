# Peak element
# https://practice.geeksforgeeks.org/problems/peak-element/1

def peakElement(nums, n):
    low = 0
    high = n-1
    
    while low < high:
        mid = low + (high - low + 1)//2
        if (mid - 1 >= 0 and nums[mid - 1] <= nums[mid]):
            low = mid
        else:
            high = mid - 1
    return (low)
