# Longest Common Prefix in an Array
# https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1

def longestCommonPrefix(arr, n):
    longestPrefix = ""
    longestPrefixLength = 0

    for i in range(0, n):
        if len(arr[i]) > longestPrefixLength:
            longestPrefix = arr[i]
            longestPrefixLength = len(longestPrefix)

    for word in arr:
        commonCharNumber = 0

        for c in range(0, len(word)):
            if word[c] == longestPrefix[c]:
                commonCharNumber += 1
            else:
                break

        if commonCharNumber < longestPrefixLength:
            longestPrefixLength = commonCharNumber

    return -1 if longestPrefixLength == 0 else longestPrefix[0:longestPrefixLength]
