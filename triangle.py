#program to print a triangle of nos 0
def tri(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("0", end=" ")
        print(" ")
tri(10)
