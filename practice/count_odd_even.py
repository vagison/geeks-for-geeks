# Count Odd Even
# https://practice.geeksforgeeks.org/problems/count-odd-even/1

def countOddEven(arr, n):
    odd = 0
    even = 0

    for item in arr:
        if item % 2 == 0:
            even += 1

        elif item % 2 == 1:
            odd += 1

    print(odd, even)
