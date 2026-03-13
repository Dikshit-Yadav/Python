def hanoi(n, source, target, aux):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    hanoi(n-1, source, aux, target)
    print("Move disk", n, "from", source, "to", target)
    hanoi(n-1, aux, target, source)

n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'C', 'B')
