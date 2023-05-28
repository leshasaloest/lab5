from math import ceil, sqrt


def bsgs(g, h, p):
    N = ceil(sqrt(p - 1))
    tbl = {pow(g, i, p): i for i in range(N)}
    c = pow(g, N * (p - 2), p)
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]
    return None


if __name__ == '__main__':
    print(bsgs(2, 13, 23))
    print(2**bsgs(2, 13, 23) % 23)