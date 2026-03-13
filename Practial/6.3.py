f = open("numbers.txt", "r")
for line in f:
    nums = line.split()
    total = 0
    for n in nums:
        total += int(n)
    print("Sum of the numbers on this line:",total)

f.close()
