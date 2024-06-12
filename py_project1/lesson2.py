import re
import sys

for line in sys.stdin:
    line = line.strip()
    if re.search(r"\A[01]+\Z", line):
        if re.fullmatch(r"REG-EXP", line[::-1]):
             print(line)
