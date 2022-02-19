# Minimum number of jumps
# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

def minJumps(arr, n):
    currentPosition = 0
    jumpNumbers = 0
    farestPosition = currentPosition + arr[currentPosition]

    while currentPosition < n - 1:
        if n == 1:
            return 0

        if currentPosition + 1 == farestPosition + 1:
            return -1

        if farestPosition >= n - 1:
            jumpNumbers += 1
            break

        nextFarestPosition = -1
        for position in range(currentPosition + 1, farestPosition + 1):
            if currentPosition + 1 >= n - 1 or nextFarestPosition >= n - 1:
                break

            if arr[position] + position >= nextFarestPosition:
                nextFarestPosition = arr[position] + position

        currentPosition = farestPosition
        farestPosition = nextFarestPosition
        jumpNumbers += 1
    
    return jumpNumbers