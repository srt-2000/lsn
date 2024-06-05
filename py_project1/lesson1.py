import os
import os.path
with open('lesson_w.txt', 'w') as rezFile:
    for currentDir, dirs, files in os.walk('main'):
        for tmpFile in files:
            if tmpFile.endswith('.py'):
                rezFile.write(currentDir)
                rezFile.write('\n')
                break

bands = []

with open("lesson_w.txt") as fin:
    for line in fin:
        bands.append(line.strip())

bands.sort()

with open("sorted_w.txt", "w") as ft:
    for band in bands:
        ft.write(band + "\n")

