if __name__ == "__main__":
    cells = int(input())
    lanes = int(input())

    counthashtag = 0
    countcars = 0
    for i in range(lanes):
        k = input()
        kk = len(k)
        for j in range(kk):
            if k[j] == "#":
                countcars += 1
            else:
                counthashtag += 1

    print(counthashtag/(countcars + counthashtag))
