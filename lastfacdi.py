import math as m

N = int(input())
for i in range(0,N):
    inp = int(input())
    l = str(m.factorial(inp))
    print(l[-1])
