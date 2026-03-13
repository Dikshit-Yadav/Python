f = open("numbers.txt", "r")
data = f.read()
numbers = data.split()
total = 0
for n in numbers:
    total += int(n)
print("Sum of the numbers:", total)
f.close()
