import sys

if __name__ == "__main__":
    sys.stdin.readline()
    for line in sys.stdin:
        temp = line.strip("\n").split(" ")
        temp = [int(i) for i in temp]
        first_number = temp[0]
        total= 0
        for i in range(1,len(temp)):
            total += temp[i]
        average = total/first_number
        count = 0
        for i in range(1,len(temp)):
            if temp[i] > average:
                count += 1
        aboveaverage = count/temp[0]
        print("{:.3%}".format(aboveaverage))
