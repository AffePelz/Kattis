if __name__ == "__main__":
    N = int(input())
    k = ""
    for i in range(N):
        K = input().split()
        if K[0] == "Simon" and K[1] == "says":
            K.pop(0)
            K.pop(0)
            W = ' '.join(K)
            print("", W)
