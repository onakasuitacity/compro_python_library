# https://atcoder.jp/contests/abc045/tasks/abc045_b
a,b,c = [input() for _ in range(3)]
i,j,k = 0,0,0
turn = 'a'

while(True):
    if turn=='a':
        if i>=len(a): break
        turn = a[i]
        i+=1
    elif turn=='b':
        if j>=len(b): break
        turn = b[j]
        j+=1
    else:
        if k>=len(c): break
        turn = c[k]
        k+=1
        
print(turn.upper())
