## Source: https://adventofcode.com/2020/day/22

fileobj = open("input22.txt", "r")

p1 = [lines.rstrip('\n') for lines in fileobj.readlines()]
p2 = p1[p1.index("Player 2:")+1:]
p1 = p1[p1.index("Player 1:")+1:p1.index("")]
p2 = [int(x) for x in p2]
p1 = [int(x) for x in p1]
# print("p1: {}\np2: {}".format(p1, p2))

ans = 0
while len(p1) != 0 and len(p2) != 0:
    if p1[0] > p2[0]:
        e1 = p1.pop(0)
        e2 = p2.pop(0)
        p1.append(e1)
        p1.append(e2)
    else:
        e1 = p2.pop(0)
        e2 = p1.pop(0)
        p2.append(e1)
        p2.append(e2)

if len(p1) == 0:
    for i in range (len(p2)):
        ans += (i+1)*p2[-(i+1)]
else:
    for i in range (len(p1)):
        ans += (i+1)*p1[-(i+1)]

print("Sum of products: {}".format(ans))
