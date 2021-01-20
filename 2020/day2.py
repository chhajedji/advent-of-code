## Source: https://adventofcode.com/2020/day/2

fileobj = open("input2.txt", "r")

valid_p1 = 0
valid_p2 = 0

while True:
    line = fileobj.readline().rstrip()
    # EoF check
    if len(line) == 0:
        break
    linearr = line.split(" ")
    low = int(linearr[0].split("-")[0])
    hi = int(linearr[0].split("-")[1])
    char = str(linearr[1].split(":")[0])
    target = str(linearr[2])
    # Part 2
    var1 = (target[low-1] == char)
    var2 = (target[hi-1] == char)
    valid_p2 += (var1 ^ var2)
    # Part 1
    if low <= target.count(char) and target.count(char) <= hi:
        valid_p1 += 1

print("valid part 1: {}\nvalid part 2: {}".format(valid_p1, valid_p2));
