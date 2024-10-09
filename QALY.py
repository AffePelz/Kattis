N = int(input())
s = 0
for i in range(0,N):
    inp = input().split()
    q = float(inp[0])
    y = float(inp[1])
    s += q*y
print('{:.3f}'.format(s))
