# https://atcoder.jp/contests/abc021/tasks/abc021_b
def resolve():
    n=int(input())
    a,b=map(int,input().split())
    k=int(input())
    A=set(map(int,input().split()))|{a,b}
    print("YES" if len(A)==(k+2) else "NO")
resolve()
