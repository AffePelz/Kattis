if __name__ == "__main__":
    inp = input().split()
    c = int(inp[0])
    totalsum = int(inp[1])

    for i in range(0,c):
        k = int(input())
        totalsum -= k
    if totalsum >= 0:
        print("Jebb")
    else:
        print("Neibb")
