inp = input().split()[0]

if __name__ == "__main__":
    vowels = ["a", "e", "i", "o", "u"]
    count1 = 0
    count2 = 0
    l = len(inp)
    for i in range(0,l):
        if inp[i] in vowels:
            count1 += 1
            count2 += 1
        elif inp[i] == "y":
            count2 += 1
    print(count1, count2)
