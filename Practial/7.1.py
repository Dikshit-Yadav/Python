strings = ["apple", "banana", "cherry", "mango"]

f = open("strings.txt", "w")

for s in strings:
    f.write(s + "\n")
    print(s)
f.close()