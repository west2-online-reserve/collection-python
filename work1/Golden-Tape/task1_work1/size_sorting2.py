x, y, z = map(int, input("给三个整数，用空格分隔: ").split())

maximum = max(x, y, z)
minimum = min(x, y, z)
middle = x + y + z - maximum - minimum

print(maximum, middle, minimum)