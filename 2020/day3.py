# Source: https://adventofcode.com/2020/day/3

from functools import reduce

fileobj = open("input3.txt", "r")

RINC = [1, 3, 5, 7, 1]
DINC = [1, 1, 1, 1, 2]
map = [lines.rstrip('\n') for lines in fileobj.readlines()]
# print(map)

count, ri, di = [0 for i in range (5)], 0, 0

for i in range (5):
    ri, di = 0, 0
    while di != len(map)-1:
        if (ri >= len(map[di-1])) :
            ri %= len(map[di-1])
        if map[di][ri] == "#":
            count[i] += 1
        ri += RINC[i]
        di += DINC[i]

print("trees in part 1: {}\nproduct in part 2: {}".format(count[1], reduce((lambda a, b: a*b), count)))
