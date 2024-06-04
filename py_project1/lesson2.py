with open("dataset_24465_4.txt", "r") as f:
    n = f.read()
    n = n.splitlines()
    n.reverse()
with open("lesson_w.txt", "w") as w:
    k = "\n".join(n)
    w.write(k)
