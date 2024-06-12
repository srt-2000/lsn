s, t = (input() for _ in range(2))
def f(s, t):
    cnt = 0
    for n in range(len(s)):
        if s.startswith(t, n):
            cnt += 1
    return cnt

print(f(s, t))