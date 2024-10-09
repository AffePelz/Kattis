N = int(input())
inp = input().split(" ")

if __name__ == "__main__":
    num = 0
    for i in inp:
        if int(i) < 0:
            num += 1

print(num)