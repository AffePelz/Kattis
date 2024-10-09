first = int(input().split()[0])

if __name__ == "__main__":
    maxpoint = 0
    for i in range(first):
        k = input().split()
        name = k[0]
        points = int(k[1])
        if maxpoint < points:
            maxname = name
            maxpoint = points
    print(maxname)
