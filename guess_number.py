import sys

if __name__ == "__main__":
    start = 1
    end = 1001
    mid = (end - start) // 2
    count = 0
    while True:

        print(mid)

        inpt = input()
        if inpt == "lower":
            end = mid
            mid = start + (end - start) // 2

        elif inpt == "higher":
            start = mid
            mid = start + (end - start) // 2

        elif inpt == "correct":
            break
