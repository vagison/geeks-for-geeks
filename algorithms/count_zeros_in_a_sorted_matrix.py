# Count zeros in a sorted matrix
# https://practice.geeksforgeeks.org/problems/count-zeros-in-a-sorted-matrix/1

def countZeroes(self, arr, n):
    row = n - 1
    col = 0
    total = 0

    while (row >= 0 and col < n):
        if(arr[row][col] == 0):
            total += (row+1)
            col += 1
        elif(arr[row][col] == 1):
            row -= 1

    return total
