import math as m

if __name__ == "__main__":
    N = int(input().split(" ")[0])
    if N > 14:
        print(m.e)
    else:
        s = 0
        for i in range(0,N+1):
            s += 1/(m.factorial(i))
    
        print(s)