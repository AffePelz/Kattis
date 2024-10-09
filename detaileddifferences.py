if __name__ == "__main__":
    inp = int(input())

    i = 1
    error = ""
    while i <= inp:
        j = input()
        k = input()
        l = len(j)

        for m in range(l):
            if j[m] == k[m]:
                error += "."
            else:
                error += "*"

        print(j)
        print(k)
        print(error)
        print("")
        error = ""
        i += 1
