import math as m
if __name__ == "__main__":
    N = int(input())
    g = 9.81
    for i in range(0,N):
        inp = input().split()
        v0 = float(inp[0])
        theta = (float(inp[1])*m.pi)/180
        x1 = float(inp[2])
        h1 = float(inp[3])
        h2 = float(inp[4])
        time = x1/(v0*m.cos(theta))
        y = v0*time*m.sin(theta) - 1/2*g*time**2
        if (y - h1) >= 1 and (h2 - y) >= 1:
            print("Safe")
        else:
            print("Not Safe")
