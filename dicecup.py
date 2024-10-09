inp = input().split()
N = int(inp[0])
M = int(inp[1])

if __name__ == "__main__":
    comb = []
    for i in range(1,N+1):
        for j in range(1,M+1):
            k = i + j
            comb.append(k)

    new_dict = {i : comb.count(i) for i in comb}
    for i in range(2,N+M+1):
        if new_dict[i] == min(M,N):
            print(i)
