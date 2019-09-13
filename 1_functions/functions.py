# prime factorization
def trial_division(n):
    factor=[]
    sqrt=int(n**.5)+1 # sqrt=ceil(sqrt(n))
    for num in range(2,sqrt):
        while n % num == 0:
            n //= num
            factor.append(num)
    if n==1: return factor
    else: return factor+[n]

n,k=map(int,input().split())
primes=trial_division(n)

# n進数
def nsin(x, n):
    if(int(x/n)):
        return nsin(int(x/n),n)+str(x%n)
    return str(x)

# Eratosthenes Sieve (O(nloglogn))
def is_prime(n):
    if n<=1: return False
    A = [i for i in range(2, n+1)]
    P = []
    lim = n**.5
    while True:
        prime = A[0]
        if prime > lim: break
        P.append(prime)
        i = 0
        while i < len(A): # for loopを使わないのは、popでindexがズレるため
            if A[i] % prime == 0:
                A.pop(i)
                continue
            i += 1
    for a in A:
        P.append(a)
    return n in P
