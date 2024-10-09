if __name__ == "__main__":
    inp = input().split()
    m = int(inp[0])
    n = int(inp[1])

    lis = []
    for i in range(m):
        k = input().split()
        lis.append(k)

    lis2 = []
    for i in range(1,m-1):
        for j in range(1,n-1):
            k = int(lis[i][j])
            if k < int(lis[i-1][j]) and k < int(lis[i+1][j]) and k < int(lis[i][j-1]) and k < int(lis[i][j+1]):
                lis2.append("Jebb")
            else:
                lis2.append("Neibb")

    if "Jebb" in lis2:
        print("Jebb")
    else:
        print("Neibb")
