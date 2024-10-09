if __name__ == "__main__":
    inp = input().split()
    R = int(inp[0])
    C = int(inp[1])

    l = []
    for k in range(R):
        m = input()
        l.append(m)

    count0 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for i in range(0,R-1):
        for j in range(0,C-1):
            a = l[i][j]
            b = l[i][j+1]
            c = l[i+1][j]
            d = l[i+1][j+1]
            if a == "#" or b == "#" or c == "#" or d == "#":
                continue
            elif a == b == c == d == "X":
                count4 += 1
            elif a == b == c == d == ".":
                count0 += 1
            elif (a == "X" and b == c == d == ".") or (b == "X" and a == c == d == ".") or (c == "X" and b == a == d == ".") or (d == "X" and b == c == a == "."):
                count1 += 1
            elif (b == c == d == "X") or (a == c == d == "X") or (a == b == d == "X") or (c == b == a == "X"):
                count3 += 1
            elif (a == b == "X") or (c == b == "X") or (c == d == "X") or (a == d == "X") or (d == b == "X") or (a == c == "X"):
                count2 += 1

    print(count0)
    print(count1)
    print(count2)
    print(count3)
    print(count4)
