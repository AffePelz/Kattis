inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])
d = int(inp[3])
e = int(inp[4])

score = int(input())
if score >= a:
    print("A")
elif score >= b and score < a:
    print("B")
elif score >= c and score < b:
    print("C")
elif score >= d and score < c:
    print("D")
elif score >= e and score < d:
    print("E")
elif score < e:
    print("F")
