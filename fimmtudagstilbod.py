inp = int(input())

if __name__ == "__main__":
    start = 2020
    originalprice = 1000
    inc = 100
    years = inp - start
    for i in range(years):
        originalprice += 100
    print(originalprice)
