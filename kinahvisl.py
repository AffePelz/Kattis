first = input().split()[0]
second = input().split()[0]

if __name__ == "__main__":
    count = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            count += 1
    print(count + 1)
