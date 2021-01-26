## Source: https://adventofcode.com/2020/day/5

score = 0
seats = [0 for i in range(128*8)]
fileobj = open("input5.txt", "r")

line = fileobj.readline().rstrip()

while line:
    col, row = 0, 0
    lo, hi = 0, 127
    row = int((lo+hi)/2)
    for i in range(7):
        if (line[i] == 'F'):
            hi = row
        else:
            lo = row+1
        row = int((lo+hi)/2)

    lo, hi = 0, 7
    col = int((lo+hi)/2)
    for i in range(3):
        if (line[7+i] == 'L'):
            hi = col
        else:
            lo = col+1
        col = int((lo+hi)/2)

    new_score = (row*8)+col
    # Block the booked seat.
    seats[new_score] = new_score
    if row == 0 or row == 127:
        seats[new_score] = new_score
    score = max(new_score, score)

    line = fileobj.readline().rstrip()

i = 0
for i in range (1024):
    if (seats[i] != 0 and seats[i+1] == 0 and seats[i+2] != 0):
        myseat = i+1
        break
print("Max score: {}\nMy ID: {}".format(score, i+1))
