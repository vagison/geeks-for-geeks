# Jump Game
# https://practice.geeksforgeeks.org/problems/jump-game/1

def canReach(A, N):
    currentPosition = 0
    jumpNumbers = 0
    farestPosition = currentPosition + A[currentPosition]

    while currentPosition < N - 1:

        if N == 1:
            return 0

        if currentPosition + 1 == farestPosition + 1:
            return 0

        if farestPosition >= N - 1:
            jumpNumbers += 1
            break

        nextFarestPosition = -1
        for position in range(currentPosition + 1, farestPosition + 1):
            if currentPosition + 1 >= N - 1 or nextFarestPosition >= N - 1:
                break

            if A[position] + position >= nextFarestPosition:
                nextFarestPosition = A[position] + position

        currentPosition = farestPosition
        farestPosition = nextFarestPosition
        jumpNumbers += 1

    if farestPosition >= N-1:
        return 1

    else:
        return 0
