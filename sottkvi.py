if __name__ == "__main__":
    inp = input().split()
    n = int(inp[0])
    k = int(inp[1])
    d = int(inp[2])

    quarantine = 14
    guestavailable = 0
    for i in range(n):
        guest = int(input())
        if guest + quarantine <= d + k:
            guestavailable += 1
        else:
            continue

    print(guestavailable)
