inp = input().split(" ")
key = set(inp)

if __name__ == "__main__":
    if len(inp) != len(key):
        print("no")
    else:
        print("yes")