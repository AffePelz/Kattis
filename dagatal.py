input = int(input())

if __name__ == "__main__":
    if input == 2:
        print(28)
    elif input > 7 and input%2 == 0:
        print(31)
    elif input > 7 and input%2 == 1:
        print(30)
    elif input <= 7 and input%2 == 1:
        print(31)
    elif input <= 7 and input%2 == 0:
        print(30)