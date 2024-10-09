N = list(input())

if __name__ == "__main__":
    while N[0] != "a":
        if N[0] == "a":
            break
        else:
            N.remove(N[0])
    x = ""
    for i in N:
        x += i
    print(x)
