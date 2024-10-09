if __name__ == "__main__":
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(input().split())

    direct = 0
    for i in range(n):
        for j in range(n):
            if int(matrix[i][j]) != -1:
                direct += 1

    print(direct)
    for i in range(n):
        for j in range(n):
            if int(matrix[i][j]) != -1:
                print(i+1, j+1, matrix[i][j])
