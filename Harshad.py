N = int(input())
s = 0
for i in str(N):
    s += int(i)

i = True
while i:
    if N%s == 0:
        print(N)
        i = False
    else:
        N += 1
        s = 0
        for i in str(N):
            s += int(i)
