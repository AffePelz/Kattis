word = input().split()[0]

if __name__ == "__main__":
    l = len(word)
    countb = 0
    countk = 0
    for i in range(l):
        if word[i] == "b":
            countb += 1
        elif word[i] == "k":
            countk += 1

    if countb > countk:
        print("boba")
    elif countb < countk:
        print("kiki")
    elif countb == countk and countk != 0:
        print("boki")
    else:
        print("none")
