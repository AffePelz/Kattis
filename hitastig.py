inp = int(input())
inp2 = input().split()

if __name__ == "__main__":
    min = int(inp2[0])
    max = int(inp2[0])
    for i in range(1,inp):
        k = int(inp2[i])
        if k >= max:
            max = k
        elif k <= min:
            min = k

    print(max, min)
