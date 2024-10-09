if __name__ == "__main__":
    X = int(input())
    N = int(input())
    s = X
    for i in range(0,N):
        spent = int(input())
        s += (X - spent)
    print(s)
