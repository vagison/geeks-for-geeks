# Intersection of two arrays
# https://practice.geeksforgeeks.org/problems/intersection-of-two-arrays2404/1

def numberofElementsInIntersection(a, b, n, m):
    def solver(shortest, longest):
        hashMap = {}
        counter = 0

        for element in shortest:
            if not (element in hashMap):
                hashMap[element] = 1
            else:
                hashMap[element] += 1

        for element in longest:
            if element in hashMap and hashMap[element] > 0:
                counter += 1
                hashMap[element] = 0

        return counter

    return (solver(a, b) if n < m else solver(b, a))
