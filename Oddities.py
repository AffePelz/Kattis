N = int(input())
for i in range(0,N):
    inp = int(input())
    if abs(inp)%2 == 0:
        print(f'{inp} is even')
    else:
        print(f'{inp} is odd')
