N = int(input())

if __name__ == "__main__":
    if N%2 == 1:
        print("Either")
    elif N%4 == 2:
        print("Odd")
    else:
        print("Even")