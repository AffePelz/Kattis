if __name__ == "__main__":
    N = 5
    contestants = {}
    for i in range(1,N+1):
        inp = input().split(" ")
        s = 0
        for j in inp:
            s += int(j)
            contestants[i] = s

    max_key = max(contestants, key=contestants.get)
    all_values = contestants.values()
    max_value = max(all_values)
    print(max_key, max_value)
