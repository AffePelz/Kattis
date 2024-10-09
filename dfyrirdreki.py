a = int(input())
b = int(input())
c = int(input())

if __name__ == "__main__":
    roots = b**2 - 4*a*c
    if roots > 0:
        print(2)
    elif roots < 0:
        print(0)
    else:
        print(1)
