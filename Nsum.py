import sys

if __name__ == "__main__":
    n = sys.stdin.readline()
    N = int(n)
    for line in sys.stdin:
        temp = line.split()
        s = 0
        for i in range(0,N):
            s += int(temp[i])
        print(s)
