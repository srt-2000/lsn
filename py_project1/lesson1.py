f = open("lesson_test.txt")
for line in f:
    line = line.rstrip()
    print(repr(line))
f.close()