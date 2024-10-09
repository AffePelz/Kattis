C = float(input())
L = int(input())
s = 0
for i in range(0,L):
    inp = input().split()
    w = float(inp[0])
    l = float(inp[1])
    s += w*l

final = s*C
print('{:.7f}'.format(final))
