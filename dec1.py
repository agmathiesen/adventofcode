with open('input1.txt', 'r') as f:
    numbers = [int(i) for i in ''.join(f.readlines()).strip()]
    count1 = 0
    count2 = 0
    for i in range(len(numbers)):
        c0 = numbers[i]
        c1 = numbers[(i+1) % len(numbers)]
        c2 = numbers[(i+ (len(numbers)//2)) % len(numbers)]
        if (c0 == c1):
            count1 += c0
        if (c0 == c2):
            count2 += c0

print(count1)
print(count2)
                
        
f.close()
