# Gray Code
# https://practice.geeksforgeeks.org/problems/gray-code-1611215248/1/

def graycode(n):
    def convertStringToList(string):
        resultingList = []
        resultingList[:0] = string
        return resultingList

    baseList = ["0" * n]

    for i in range(n - 1, -1, -1):
        listLastIndex = len(baseList) - 1
        for j in range(listLastIndex, -1, -1):
            stringToList = convertStringToList(baseList[j])
            stringToList[i] = "1"
            listToString = ''.join(stringToList)
            baseList.append(listToString)

    return baseList
