# 3 = I like this problem
# -3 = I don't like this problem
# 0 = I don't care about this problem
# First number of first line  = number of judges
# Second number of first line = number of judges who have already rated the problem

if __name__ == "__main__":
    inp = input().split()
    Judges = int(inp[0])
    Rated = int(inp[1])
    r_max = []
    r_min = []
    for i in range(0,Rated):
        rating_number = int(input())
        r_max.append(rating_number)
        r_min.append(rating_number)

    # max
    Max_rating = 3
    Min_rating = -3
    for i in range(Rated, Judges):
        if len(r_max) != Judges:
            r_max.append(Max_rating)
            r_min.append(Min_rating)
        else:
            break

    sum1 = 0
    sum2 = 0
    for i in r_min:
        sum1 += i

    for i in r_max:
        sum2 += i

    print(sum1/Judges, sum2/Judges)
