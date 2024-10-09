inp = input().split()
n = int(inp[0])
h = int(inp[1])
v = int(inp[2])

if __name__ == "__main__":
    fix1 = n - h
    fix2 = n - v

    biglength = max(h,fix1)
    bigwidth = max(v,fix2)
    thick = 4
    volume = bigwidth*biglength*4

    print(volume)
