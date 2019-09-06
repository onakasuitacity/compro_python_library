# https://atcoder.jp/contests/abc115/tasks/abc115_d
def resolve():
    n,x=map(int,input().split())
    L=[1]*51
    for i in range(1,51):
        L[i]=3+2*L[i-1]
    def f(l,x,L):
        if l==0:
            return x
        elif x<=1:
            return 0
        elif x<=1+L[l-1]:
            return f(l-1,x-1,L)
        elif x==2+L[l-1]:
            return 1+f(l-1,L[l-1],L)
        elif x<=2+2*L[l-1]:
            return 1+f(l-1,L[l-1],L)+f(l-1,x-2-L[l-1],L)
        else:
            return 1+2*f(l-1,L[l-1],L)
    print(f(n,x,L))
resolve()
