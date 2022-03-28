# Product array puzzle
# https://practice.geeksforgeeks.org/problems/product-array-puzzle4525/1

def productExceptSelf(nums, n):
    if n == 1:
        return [1]

    else:
        leftToRight = [nums[0]]
        rightToLeft = [nums[n - 1]]

        for i in range(1, n):
            leftToRight.append(leftToRight[i - 1] * nums[i])

        for i in range(0, n-1):
            rightToLeft.append(rightToLeft[i] * nums[n - 2 - i])

        rightToLeft = rightToLeft[::-1]

        returnedArray = [rightToLeft[1]]
        for i in range(1, n - 1):
            returnedArray.append(leftToRight[i - 1] * rightToLeft[i + 1])
        returnedArray.append(leftToRight[n - 2])

        return returnedArray
