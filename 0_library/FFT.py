from cmath import pi, rect
def _fft(A, inverse = False):
    step = N
    for k in range(logN):
        step >>= 1
        w = rect(1, pi / (1 << k) * (1 - 2 * inverse))
        wj = 1
        nA = [0] * N
        for j in range(1 << k):
            for i in range(1 << logN - k - 1):
                s, t = i + j * step, i + j * step + (N >> 1)
                ps, pt = i + j * step * 2, i + j * step * 2 + step
                nA[s], nA[t] = A[ps] + A[pt] * wj, A[ps] - A[pt] * wj
            wj *= w
        A = nA
    return A
 
def convolution(f, g):
    Ff, Fg = _fft(f + [0] * (N - len(f))), _fft(g + [0] * (N - len(g)))
    fg = _fft([a * b / N for a, b in zip(Ff, Fg)], inverse = True)
    del fg[len(f) + len(g) - 1:]
    return fg
