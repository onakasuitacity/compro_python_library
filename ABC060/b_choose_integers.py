# https://atcoder.jp/contests/abc060/tasks/abc060_b
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
 
a,b,c = map(int,input().split())
print("YES") if c%gcd(a,b)==0 else print("NO")
