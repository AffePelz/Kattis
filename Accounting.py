from collections import defaultdict

if __name__ == "__main__":
    n, m = input().split()
    d = defaultdict(lambda: 0)
    for _ in range(int(m)):
        command = input().split(" ")

        if command[0] == "SET":
            d[command[1]] = command[2]

        elif command[0] == "PRINT":
            print(d[command[1]], flush = True)

        elif command[0] == "RESTART":
            t = command[1]
            d = defaultdict(lambda: t)
