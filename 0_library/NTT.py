prime = 998244353
root = 3
def _fmt(A, inverse = False):
    N = len(A)
    logN = (N - 1).bit_length()
    base = pow(root, (prime - 1) // N * (1 - 2 * inverse) % (prime - 1), prime)
    step = N
    for k in range(logN):
        step >>= 1
        w = pow(base, step, prime)
        wj = 1
        nA = [0] * N
        for j in range(1 << k):
            for i in range(1 << logN - k - 1):
                s, t = i + j * step, i + j * step + (N >> 1)
                ps, pt = i + j * step * 2, i + j * step * 2 + step
                nA[s], nA[t] = (A[ps] + A[pt] * wj) % prime, (A[ps] - A[pt] * wj) % prime
            wj = (wj * w) % prime
        A = nA
    return A
 
def convolution(f, g):
    N = 1 << (len(f) + len(g) - 2).bit_length()
    Ff, Fg = _fmt(f + [0] * (N - len(f))), _fmt(g + [0] * (N - len(g)))
    N_inv = pow(N, prime - 2, prime)
    fg = _fmt([a * b % prime * N_inv % prime for a, b in zip(Ff, Fg)], inverse = True)
    del fg[len(f) + len(g) - 1:]
    return fg
