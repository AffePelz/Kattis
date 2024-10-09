def sorting_count(A):
    n = len(A)
    c = 0
    for i in range(0,len(A)-1):
        for j in range(0,len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                c += 1
    return c

if __name__ == "__main__":
    N = int(input())
    for _ in range(0,N):
        tmp = input().split(" ")
        arr = list(map(int, tmp))
        print(arr[0], sorting_count(arr[1:]))
