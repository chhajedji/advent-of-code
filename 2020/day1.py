## Source: https://adventofcode.com/2020/day/1

fileobj = open("input1.txt", "r")
nums = [int(lines.rstrip('\n')) for lines in fileobj.readlines()]

# print(content)

## Part 1

done = 0
for i in range(len(nums)-1):
    n1 = nums[i]
    n2 = 2020-n1
    if done == 1:
        break
    for j in range (i+1, len(nums), 1):
        if (nums[j] == n2):
            print("Numbers are: {}, {}".format(n1, n2))
            print("Product of pair is {}".format(nums[i]*nums[j]))
            done = 1
            break

## Part 2

done = 0
for i in range (len(nums)-2):
    n1 = nums[i]
    if done == 1:
        break
    for j in range(i+1, len(nums)-1):
        n2 = nums[j]
        n3 = 2020-n1-n2
        if done == 1:
            break
        for k in range (j+1, len(nums), 1):
            if (nums[k] == n3):
                print("Numbers are: {}, {}, {}".format(n1, n2, n3))
                print("Product of triplet is {}".format(n1*n2*n3))
                done = 1
                break
