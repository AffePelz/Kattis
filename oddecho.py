inp = input()
N = int(inp)

if __name__ == "__main__":
    lst = []
    for i in range(0,N):
        inp1 = input()
        lst.append(inp1)

    for i in range(0,N):
        if i%2 == 0:
            print(lst[i])
