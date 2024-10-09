N = 10

lst = set()
for i in range(0,N):
    inp = int(input())
    lst.add(inp%42)

print(len(lst))
