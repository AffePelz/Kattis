N = int(input())

if __name__ == "__main__":
    for i in range(0,N):
        inp = input().split(" ")
        a = int(inp[0])
        b = int(inp[1])
        c = int(inp[2])
        
        if ((a + b) == c) or ((a - b) == c) or ((a * b) == c) or ((a / b) == c):
            print("Possible")
        elif ((b + a) == c) or ((b - a) == c) or ((b * a) == c) or ((b / a) == c):
            print("Possible")
        else:
            print("Impossible")