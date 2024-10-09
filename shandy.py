Beer = int(input())
Lemonade = int(input())

if __name__ == "__main__":
    mix = 0
    f = True
    while f:
        if Beer == 0 or Lemonade == 0:
            f = False
        else:
            Beer -= 1
            Lemonade -= 1
            mix += 2
    print(mix)
