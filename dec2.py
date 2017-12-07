with open("input3.txt", "r") as f:
    rows = [r.strip() for r in f.readlines()]
    count = 0
    count2 = 0
    for p in range(len(rows)):
        numbers = sorted([int(x) for x in rows[p].split()])
        count += numbers[-1] - numbers[0]
        for n in range(len(numbers)):
            x = numbers[n]
            for m in range(n, len(numbers)-n):
                y = numbers[m+n]
                if ((y % x == 0) & (y != x)):
                    count2 += y//x
    print(count)
    print(count2)
f.close()
