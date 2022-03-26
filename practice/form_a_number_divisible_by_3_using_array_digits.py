# Form a number divisible by 3 using array digits
# https://practice.geeksforgeeks.org/problems/form-a-number-divisible-by-3-using-array-digits0717/1

def isPossible(N, arr):
    descriptor = 0

    for index in range(0, N):
        descriptor += (arr[index] % 3)

    return(1 if descriptor % 3 == 0 else 0)
