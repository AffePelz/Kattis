import sys

for line in sys.stdin:
    temp = line.strip("\n").split(" ")
    temp = [int(i) for i in temp]
    while temp != [1,2,3,4,5]:
        for i in range(0,len(temp)-1):
            if temp[i] > temp[i+1]:
                temp[i], temp[i+1] = temp[i+1], temp[i]
                print(*temp)
