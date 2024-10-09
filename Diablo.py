import sys
import math

for line in sys.stdin:
    temp = line.strip("\n").split(" ")
    A = float(temp[0])
    N = float(temp[1])
    radius = N / (math.pi * 2)
    areal = math.pi*radius**2
    if areal >= A:
        print("Diablo is happy!")
    else:
        print("Need more materials!")
