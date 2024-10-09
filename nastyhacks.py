n = int(input())

if __name__ == "__main__":
    for i in range(0,n):
        inp = input().split()
        r = int(inp[0])
        e = int(inp[1])
        c = int(inp[2])
        s = e - r
        if s > c:
            print('advertise')
        elif s == c:
            print('does not matter')
        else:
            print('do not advertise')
