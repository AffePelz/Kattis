if __name__ == "__main__":
    inp = input().split()
    N = int(inp[0])
    M = int(inp[1])

    word = ""
    for i in range(N):
        k = input()
        for j in range(M):
            if k[j] != ".":
                word += k[j]

    print(word)
