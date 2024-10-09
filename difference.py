import sys

def diff(a,b):
    return abs(a - b)

for line in sys.stdin:
    temp = line.strip("\n").split(" ")
    nums1 = int(temp[0])
    nums2 = int(temp[1])
    print(diff(nums1,nums2))
