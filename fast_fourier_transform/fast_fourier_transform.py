from cmath import pi, rect
def _fft(f, inverse=False):
    N = len(f)
    logN = (N - 1).bit_length()
    step = N
    for k in range(logN):
        step >>= 1
        w = rect(1, pi / (1 << k) * (1 - 2 * inverse))
        wj = 1
        nf = [0] * N
        for j in range(1 << k):
            for i in range(1 << logN - k - 1):
                s, t = i + 2 * j * step, i + (2 * j + 1) * step
                ns, nt = i + j * step, i + j * step + (N >> 1)
                nf[ns], nf[nt] = f[s] + f[t] * wj, f[s] - f[t] * wj
            wj *= w
        f = nf
    if inverse:
        f = [a / N for a in f]
    return f

def convolve(f, g):
    N = 1 << (len(f) + len(g) - 2).bit_length()
    Ff, Fg = _fft(f + [0] * (N - len(f))), _fft(g + [0] * (N - len(g)))
    fg = _fft([a * b for a, b in zip(Ff, Fg)], inverse = True)
    del fg[len(f) + len(g) - 1:]
    return fg
