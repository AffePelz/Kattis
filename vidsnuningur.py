input = input().split()

if __name__ == "__main__":
    letter = input[0]
    l = len(letter)
    k = ""

    for i in range(1,l+1):
        k += letter[-i]

    print(k)
