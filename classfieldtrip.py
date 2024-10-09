if __name__ == "__main__":
    K = input()
    L = input()

    newword = K + L
    m = "".join(sorted(newword))
    print(m)
