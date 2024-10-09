N = int(input())

if __name__ == "__main__":
    x = []
    for i in range(0,N):
        x.append(int(input()))
        
    for j in x[::-1]:
        print(j)