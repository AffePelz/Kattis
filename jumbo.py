# no train more than 40 hours a day
# fusing two rods will lose 1 cm in combined length

N = int(input().split(" ")[0])
l1 = int(input().split(" ")[0])
comb_length = l1
for i in range(0,N-1):
    li = int(input().split(" ")[0])
    comb_length += li
    comb_length -= 1
print(comb_length)
