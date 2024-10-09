import math as m

inp = input().split(" ")
N = int(inp[0])
W = int(inp[1])
H = int(inp[2])
hypotenus = int(m.sqrt(H**2 + W**2))
for i in range(0,N):
    l = int(input().split(" ")[0])
    if l <= W or l <= H or l <= hypotenus:
        print("DA")
    else:
        print("NE")
