if __name__ == "__main__":
    inp = input().split(" ")[0]
    N = int(inp)

    trylearn = input().split(" ")
    learned = input().split(" ")

    for i in trylearn:
        if i not in learned:
            print(i)
