first = input().split()

if __name__ == "__main__":
    full = [1,1,2,2,2,8]
    l = len(full)
    m = []
    for i in range(0,l):
        answer = full[i] - int(first[i])
        m.append(answer)
    
    print(m[0], m[1], m[2], m[3], m[4], m[5])
        