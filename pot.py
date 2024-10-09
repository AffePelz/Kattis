if __name__ == "__main__":
    N = int(input())
    sum = 0
    for i in range(0,N):
        k = input()
        sum += int(k[0:-1])**int(k[-1])

    print(sum)
