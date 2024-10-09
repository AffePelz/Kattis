if __name__ == "__main__":
    inp = input().split(" ")
    k = int(inp[0])
    m = int(inp[1])
    n = int(inp[2])
    
    if k%(m+n) < m:
        print("Barb")
    else:
        print("Alex")
