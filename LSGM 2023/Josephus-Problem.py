def josephus_permutation(n: int, k: int) -> list[int]:
    l = [i for i in range(1, n + 1)]
    if k == 1: return l
    r = []
    i = 0
    while len(l) > 0:
        i += k - 1
        if i >= len(l):
            i = i % len(l)
        r.append(l.pop(i))
    return r


def josephus_last2(n: int) -> int:
    return (n << 1) - (2 ** n.bit_length()) + 1

def josephus_last(n: int, k: int) -> int:
    if n == 1: return 1
    if k == 2: return josephus_last2(n)
    return ((josephus_last(n - 1, k) + k - 1) % n) + 1


print(josephus_permutation(8, 2))

print(josephus_last(1240110420214, 2))