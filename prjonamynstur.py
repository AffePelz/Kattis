if __name__ == "__main__":
    inp = input().split()
    m = int(inp[0])
    n = int(inp[1])
    #chr(92):

    dict = {"." : 20, "O" : 10, chr(92) : 25, "/" : 25, "A" : 35, "^" : 5, "v" : 22}

    points = 0
    for i in range(m):
        k = input()
        nk = [x for x in k]
        for j in nk:
            points += dict[j]

    print(points)
