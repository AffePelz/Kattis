L = input()
D = input()
X = input()

L_list = [*L]
D_list = [*D]
X_list = [*X]

l = []
for i in range(int(L),int(D)+1):
    d = str(i)
    d_list = [*d]
    s = 0
    for j in d_list:
        s += int(j)
    if s == int(X):
        l.append(i)

if __name__ == "__main__":
    print(l[0])
    print(l[-1])
