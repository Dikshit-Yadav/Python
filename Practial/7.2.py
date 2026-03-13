strings = ["apple", "banana", "cherry", "mango"]

f = open("strings.txt", "w")

line = ",".join(strings)
f.write(line)
print(line)
f.close()
