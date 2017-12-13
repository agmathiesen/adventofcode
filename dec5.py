with open("input5.txt", "r") as f:
    steps = [int(s.strip()) for s in f.readlines()]
    count = 0
    i = 0
    while (True):
        count += 1
        x = steps[i]
        #steps[i] += 1 for part 1
        if (x >= 3):
            steps[i] -= 1
        else:
            steps[i] += 1
        i += x
        if (i > len(steps)-1):
            break
print(count)
f.close()

# TIDY UP, GENERELIZE FOR PART 1 AND 2
