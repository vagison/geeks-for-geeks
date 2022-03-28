# Adding Ones
# https://practice.geeksforgeeks.org/problems/adding-ones3628/1

def update(self, a, n, updates, k):
    for i in range(0, k):
        if(updates[i] - 1 <= n - 1):
            a[updates[i] - 1] += 1

    for i in range(0, n - 1):
        a[i + 1] += a[i]

    return a
