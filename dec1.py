with open('input.txt', 'r') as f:
    inp = ''.join(f.readlines()).strip()
    count = 0
    for i in range(len(inp)-1):
        c0 = int(inp[i])
        c1 = int(inp[i+1])
        if (c0 == c1):
            count += c0
    if (int(inp[0]) == int(inp[-1])):
        count += int(inp[0])

print(count)
                
        
f.close()
