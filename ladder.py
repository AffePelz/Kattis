import math as m

inp = input().split(" ")
h = int(inp[0])
v = int(inp[1])

length = int(h/(m.sin(v*m.pi/180)))+1
print(length)
