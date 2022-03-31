# Counts Zeros Xor Pairs
# https://practice.geeksforgeeks.org/problems/counts-zeros-xor-pairs0349/1

def calculate(arr, n):
    arr.sort()

    counter = 0

    consideredElement = arr[0]
    amountOfConsideredElement = 1

    for i in range(1, n):
        if arr[i] == consideredElement:
            amountOfConsideredElement += 1

        else:
            counter += amountOfConsideredElement * \
                (amountOfConsideredElement - 1) // 2

            consideredElement = arr[i]
            amountOfConsideredElement = 1

    if arr[n - 1] == arr[n - 2]:
        counter += amountOfConsideredElement * \
            (amountOfConsideredElement - 1) // 2

    return counter
