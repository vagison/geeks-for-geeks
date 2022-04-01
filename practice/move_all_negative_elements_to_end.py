# Move all negative elements to end
# https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1

def segregateElements(arr, n):
    negatives = []
    positives = []

    for i in range(0, n):
        if(arr[i] < 0):
            negatives.append(arr[i])
        else:
            positives.append(arr[i])

    lenPositives = len(positives)    

    for i in range(0, lenPositives):
        arr[i] = positives[i]

    for i in range(lenPositives, n):
        arr[i] = negatives[i - lenPositives]
