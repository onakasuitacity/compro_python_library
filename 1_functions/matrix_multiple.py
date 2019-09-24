# matrix multiple (ijk-algorithm)
def mat_mul(A,B):
    assert len(A[0])==len(B)
    m=len(A)
    n=len(B)
    l=len(B[0])
    C=[[0]*l for _ in range(m)]
    for i in range(m):
        for j in range(l):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]
    return C
