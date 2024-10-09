import sys

def summation(a,b):
    return a + b

for line in sys.stdin:
    temp = line.split(" ")
    a = int(temp[0])
    b = int(temp[1])
    print(summation(a,b))
