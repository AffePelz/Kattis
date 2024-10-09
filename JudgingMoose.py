inp = input().split()
l = int(inp[0])
r = int(inp[1])

if l == r and (r == 0 or l == 0):
    print('Not a moose')
elif l == r:
    print(f'Even {max(l,r)*2}')
elif l > r or l < r:
    print(f'Odd {max(l,r)*2}')
