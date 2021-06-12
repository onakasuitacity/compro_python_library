prime = 119 << 23 | 1
root = 3
def _fmt(f, inverse=False):
    N = len(f)
    logN = (N - 1).bit_length()
    base = pow(root, (prime - 1) // N * (1 - 2 * inverse) % (prime - 1), prime)
    step = N
    for k in range(logN):
        step >>= 1
        w = pow(base, step, prime)
        wj = 1
        nf = [0] * N
        for j in range(1 << k):
            for i in range(1 << logN - k - 1):
                s, t = i + 2 * j * step, i + (2 * j + 1) * step
                ns, nt = i + j * step, i + j * step + (N >> 1)
                nf[ns], nf[nt] = (f[s] + f[t] * wj) % prime, (f[s] - f[t] * wj) % prime
            wj = (wj * w) % prime
        f = nf
    if inverse:
        N_inv = pow(N, prime - 2, prime)
        f = [a * N_inv % prime for a in f]
    return f

def convolve(f, g):
    N = 1 << (len(f) + len(g) - 2).bit_length()
    Ff, Fg = _fmt(f + [0] * (N - len(f))), _fmt(g + [0] * (N - len(g)))
    fg = _fmt([a * b % prime for a, b in zip(Ff, Fg)], True)
    del fg[len(f) + len(g) - 1:]
    return fg
