N = list(input())
vowels = ["A","E","I","O","U","a","e","i","o","u"]

if __name__ == "__main__":
    count = 0
    for i in N:
        if i in vowels:
            count += 1
    print(count)

