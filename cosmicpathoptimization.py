M = int(input())
T = input().split()

if __name__ == "__main__":
    s = 0
    for i in T:
        s += int(i)
    answer = int(s/M)
    print(answer)
