input1 = input().split()
input2 = input().split()

if __name__ == "__main__":
    n = input1[0]
    k = input1[1]
    position = input2.index(k)
    if position == 0:
        print("fyrst")
    elif position == 1:
        print("naestfyrst")
    else:
        print(position+1, "fyrst")
