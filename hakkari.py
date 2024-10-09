if __name__ == "__main__":
    inp = input().split()
    m = int(inp[0])
    n = int(inp[1])

    set = []
    countbomb = 0
    for i in range(m):
        k = input()
        nk = [x for x in k]
        set.append(nk)

    for i in range(m):
        for j in range(n):
            if set[i][j] == "*":
                countbomb += 1

    print(countbomb)
    for i in range(m):
        for j in range(n):
            if set[i][j] == "*":
                print(i+1, j+1)
