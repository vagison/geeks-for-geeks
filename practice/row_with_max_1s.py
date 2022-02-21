# Row with max 1s
# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

def rowWithMax1s(arr, n, m):
    j = m - 1
    row = -1

    for i in range(0, n):
        if j == -1:
            break

        while j > -1:
            if arr[i][j] == 1:
                row = i
                j -= 1
            else:
                break

    return row