import math as ma

inp = input().split()
r = float(inp[0])
m = int(inp[1])
c = int(inp[2])
while r != 0 and m != 0 and c != 0:
    area_circle = ma.pi*r**2
    area_square = (2*r)*(2*r)
    estimate = area_square*(c/m)
    print('{:.10}'.format(area_circle), '{:.10}'.format(estimate))
    new = input().split()
    r = float(new[0])
    m = int(new[1])
    c = int(new[2])
