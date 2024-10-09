# number of beats in 15 sec, multipli by four gives BPM
# BMP = 60*beats/p seconds
# ABPM = 60t (t is amount of time between each beat)

if __name__ == "__main__":
    N = int(input().split(" ")[0])
    for i in range(0,N):
        inp = input().split(" ")
        b = int(inp[0])
        p = float(inp[1])
        BPM = (60*b)/p
        ABPM = 60/p
        min_ABPM = BPM - ABPM
        max_ABPM = BPM + ABPM
        print('{:.4f}'.format(min_ABPM), '{:.4f}'.format(BPM), '{:.4f}'.format(max_ABPM))
