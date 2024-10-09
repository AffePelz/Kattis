input = input().split()

if __name__ == "__main__":
    v = int(input[0])
    a = int(input[1])
    t = int(input[2])
    d = v*t + 1/2*a*t**2
    print(d)