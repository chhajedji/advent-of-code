## Source: https://adventofcode.com/2020/day/24

fileobj = open("input24.txt", "r")

line = str(fileobj.readline().rstrip())

black = []
ans = 0

while line:
    x, y = 0, 0
    while len(line):
        # print("x: {}, y: {}".format(x, y))
        # print("line: ", line)
        if line[0] == 'n':
            y += 2
            if line[1] == 'e':
                x += 1
            elif line[1] == 'w':
                x -= 1
            line = line[2:]
            continue
        if line[0] == 's':
            y -= 2
            if line[1] == 'e':
                x += 1
            if line[1] == 'w':
                x -= 1
            line = line[2:]
            continue
        if line[0] == 'e':
            x += 2
            line = line[1:]
            continue
        if line[0] == 'w':
            x -= 2
            line = line[1:]
            continue
    # print("x: {}\ty: {}".format(x, y))
    black.append((x, y))

    line = fileobj.readline().rstrip()

for i in black:
    if (black.count(i) % 2):
        ans += 1

black.sort()
print("Black tiles: ", ans)
print(black)
