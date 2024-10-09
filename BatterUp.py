if __name__ == "__main__":
    N = int(input())
    inp = input().split()
    s = 0
    for i in inp:
        if i != "-1":
            s += int(i)
        else:
            N += int(i)

    print(s/N)
