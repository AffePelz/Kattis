import sys
import heapq as h

inp = sys.stdin.readline().strip("\n").split(" ")
n = int(inp[0])
m = int(inp[1])
k = int(inp[2])
time = 0

unread = [('"Jane Eyne"',k)]
friend = []

for i in range(n):
    line = sys.stdin.readline().strip("\n").split(" ")
    title = " ".join(line[:-1])
    p = int(line[-1])

    h.heappush(unread, (title,p))

for i in range(m):
    line = sys.stdin.readline().strip("\n").split(" ")
    t = int(line[0])
    title = " ".join(line[1:-1])
    p = int(line[-1])

    h.heappush(friend, (t,title,p))

jane = False

while not jane:
    while friend and time >= friend[0][0]:
        x = h.heappop(friend)[1:]
        h.heappush(unread, x)

    time += unread[0][-1]
    book = h.heappop(unread)

    if book == ('"Jane Eyne"',k):
        jane = True

print(time)
