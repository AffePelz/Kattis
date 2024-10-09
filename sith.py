if __name__ == "__main__":
    name = input()
    a = int(input())
    b = int(input())
    difference = int(input())

    if a - b < 0 and difference > 0:
        print("SITH")
    elif a - b < 0 and difference < 0:
        print("JEDI")
    elif a - b > 0 and difference > 0:
        print("VEIT EKKI")
