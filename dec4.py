with open("input4.txt", "r") as f:
    phrases = [p.strip() for p in f.readlines()]
    count1 = 0
    count2 = 0
    print(len(phrases), " passphrases in file")
    for p in range(len(phrases)):
        words = phrases[p].split()
        noDubs = set(sorted(words))
        if (len(words) == len(noDubs)):
            count1 += 1
        noAnagrams = [''.join(sorted(w)) for w in words]
        noAnagrams = set(sorted(noAnagrams))
        if (len(words) == len(noAnagrams)):
            count2 += 1
            
    print("Part 1: ", count1, " passphrases are good")
    print("Part 2: ", count2, " passphrases are good")

f.close()

