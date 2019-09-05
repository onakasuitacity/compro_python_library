# https://atcoder.jp/contests/abc062/tasks/abc062_b
def resolve():
    h,w=map(int,input().split())
    A=['#'+input()+'#' for _ in range(h)]
    print('#'*(w+2))
    print(*A,sep='\n')
    print('#'*(w+2))
resolve()
