if __name__ == "__main__":
    inp = input().split(";")
    number = 0
    for i in inp:
        if "-" in i:
            f = i.split("-")
            number += (int(f[1]) - int(f[0])) + 1
        else:
            number += 1

    print(number)
