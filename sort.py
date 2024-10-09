inp = input().split(" ")
a = int(inp[0])
b = int(inp[1])
lst = []
if __name__ == "__main__":
    if a < b:
        lst.append(a)
        lst.append(b)
    else:
        lst.append(b)
        lst.append(a)
    print(*lst)
