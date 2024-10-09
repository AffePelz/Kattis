if __name__ == "__main__":
    N = int(input())

    reversed = str(bin(N)[2:])[::-1]
    b = int(reversed,2)
    print(b)
