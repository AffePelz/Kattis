if __name__ == "__main__":
    inp = input().split()
    wc = int(inp[0])
    hc = int(inp[1])
    ws = int(inp[2])
    hs = int(inp[3])
    if (wc <= ws + 1) or (hc <= hs + 1):
        print(0)
    else:
        print(1)
