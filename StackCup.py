import heapq as h

N = int(input().split(" ")[0])
stack = []
for i in range(0,N):
    k = input().split(" ")
    try:
        radius = int(k[0])//2
        color = k[1]
        h.heappush(stack, (radius, color))
    except ValueError:
        radius = int(k[1])
        color = k[0]
        h.heappush(stack, (radius, color))
for i in sorted(stack):
    print(i[1])
