first = input().split()[0]

if __name__ == "__main__":
    k = 0
    for i in first:
        m = ord(i)
        if m >= 65 and m <= 90:
            k += 1
        elif m >= 97 and m <= 122:
            k += 1
        else:
            continue
    print(k)