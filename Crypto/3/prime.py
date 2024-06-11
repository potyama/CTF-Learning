import random

def Miller_Rabin(n):
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    s, t = 0, n-1
    while t & 1 == 0:
        s, t = s+1, t >> 1
    a = random.randint(1, n-1)
    if pow(a, t, n) == 1:
        return True
    for i in range(0, s):
        if pow(a, pow(2, i) * t, n) == n-1:
            return True
    return False

print(Miller_Rabin(999681217))
print(Miller_Rabin(999681186))
print(Miller_Rabin(140628287))
print(Miller_Rabin(140168112))

