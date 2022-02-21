# Row with max 1s
# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

def rowWithMax1s(arr, n, m):
    columnIndex = m - 1
    searchedRow = -1

    for rowIndex in range(0, n):
        if columnIndex == -1:
            break

        while columnIndex > -1:
            if arr[rowIndex][columnIndex] == 1:
                searchedRow = rowIndex
                columnIndex -= 1
            else:
                break

    return searchedRow

    