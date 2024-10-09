N = int(input())
i = 0

lst = [[] for _ in range(0,N)]
i = 0
while i < N:
    visit = int(input())
    for k in range(0,visit):
        city = input()
        if city not in lst[i]:
            lst[i].append(city)
        else:
            continue
    print(len(lst[i]))
    i += 1
