## Source: https://adventofcode.com/2020/day/4

fileobj = open("input4.txt", "r")

line = [x.rstrip() for x in fileobj.readlines()]

count2, count1, skip = 0, 0, 0
person = ""
for att in line:
    if att == "":
        final = dict((x, y)
                    for x, y in (element.split(":")
                                 for element in person.split(" ")))
        # print(final)
        if ("byr" in final and
            "iyr" in final and
            "eyr" in final and
            "hgt" in final and
            "hcl" in final and
            "ecl" in final and
            "pid" in final
        ):
            count1 += 1
            # Part 2
            if (int(final["byr"]) <= 2002 and int(final["byr"]) >= 1920 and
                int(final["iyr"]) <= 2020 and int(final["iyr"]) >= 2010 and
                int(final["eyr"]) <= 2030 and int(final["eyr"]) >= 2020 and
                final["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            ):
                if ((final["hgt"][-2:] == "cm" and
                     int(final["hgt"][:-2]) >= 150 and int(final["hgt"][:-2]) <= 193) or
                    (final["hgt"][-2:] == "in" and
                     int(final["hgt"][:-2]) >= 59 and int(final["hgt"][:-2]) <= 76)
                ):
                    if (final["hcl"][0] == "#"):
                        for letter in final["hcl"][1:]:
                            if letter not in ["a", "b", "c", "d", "e", "f",
                                    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                                skip = 1
                                break;

                        if (len(final["pid"]) == 9):
                            for num in final["pid"]:
                                if num not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                                    skip = 1
                            if  not skip:
                                count2 += 1
        person = ""
    else:
        if person != "":
            person += " " + att
        else:
            person += att

print("Valid passports: {}\nTruly valid passports: {}".format(count1, count2))
fileobj.close()
