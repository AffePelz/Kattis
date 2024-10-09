if __name__ == "__main__":
    m = int(input())
    n = int(input())
    for i in range(n):
        k = input().split()
        road = k[0]
        windroad = int(k[1])
        if windroad < m:
            print(road, "lokud")
        else:
            print(road, "opin")
