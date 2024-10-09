inp = int(input())

if __name__ == "__main__":
    n=1
    height = 0
    while True:
        inp -= n**2
        height += 1
        n += 2
        if inp - (n)**2 < 0:
            break
        else:
            continue

    print(height)
