# Lasts for eight days and eight nights
# First evening, one candle is lit. Second evening, two candles are lit and so on
# Each evening an extra candle (called the shamnas)
def sumall(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s

if __name__ == "__main__":
    N = int(input())
    s = 0
    for i in range(1,N+1):
        inp = input().split()
        day = int(inp[0])
        Chanukah = int(inp[1])
        s = sumall(Chanukah) + Chanukah
        print(day, s)
