inp = input()

if __name__ == "__main__":
    l = len(inp)
    countsmile = 0
    countsad = 0
    for i in range(l-1):
        if inp[i] == ":" and inp[i+1] == ")":
            countsmile += 1
        elif inp[i] == ":" and inp[i+1] == "(":
            countsad += 1

    if countsad == countsmile == 0:
        print("machine")
    elif countsmile == 0:
        print("undead")
    elif countsad == 0:
        print("alive")
    elif countsmile > 0 and countsad > 0:
        print("double agent")
