def _fmt(f, prime, root = 3, inverse = False):
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

def convolve(f, g, MOD):
    N = 1 << (len(f) + len(g) - 2).bit_length()
    primes = [167772161, 469762049, 1224736769]
    Ffs, Fgs = [_fmt([a % MOD for a in f] + [0] * (N - len(f)), p) for p in primes], [_fmt([b % MOD for b in g] + [0] * (N - len(g)), p) for p in primes]
    fgs = [_fmt([a * b % p for a, b in zip(Ff, Fg)], p, inverse = True) for Ff, Fg, p in zip(Ffs, Fgs, primes)]
    fg = []
    primes.append(MOD)
    for R in zip(*fgs):
        coeffs, consts = [1] * 4, [0] * 4
        for i in range(3):
            a, b, u, v = coeffs[i], primes[i], 1, 0
            while b:
                a, b, u, v = b, a - a // b * b, v, u - a // b * v
            t = (R[i] - consts[i]) * (u % primes[i]) % primes[i]
            for j in range(i + 1, 4):
                consts[j] = (consts[j] + t * coeffs[j]) % primes[j]
                coeffs[j] = coeffs[j] * primes[i] % primes[j]
        fg.append(consts[-1])
        if len(fg) == len(f) + len(g) - 1:
            return fg
