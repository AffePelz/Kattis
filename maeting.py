inp = input().split()
n = inp[0]
m = inp[1]

if __name__ == "__main__":
    Monday = input().split()
    Tuesday = input().split()
    Both = []
    for i in Monday:
        if i in Tuesday:
            Both.append(i)

    for j in Tuesday:
        if j in Monday and Both:
            continue
        elif j in Monday:
            Both.append(j)

    for i in Both:
        print(int(i), end=" ")
