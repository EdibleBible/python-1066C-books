f = open("booksq.txt", "r")
b = []
n = int(f.readline())
while (n != 0):
    sign, amount = f.readline().split()
    if sign == "L":
        b.insert(0, amount)
    elif sign == "R":
        b.append(amount)
    elif sign == "?":
        a = b.index(amount)
        print(min(a, len(b)-a-1))
    n -= 1
f.close()