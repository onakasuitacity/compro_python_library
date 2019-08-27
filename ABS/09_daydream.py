# https://atcoder.jp/contests/abs/tasks/arc065_a
import re
S = input()[::-1]
flag = True

while(S):
    m = re.match("maerd|remaerd|esare|resare", S)
    if m:
        S = S[m.end():]
    else:
        flag = False
        break
        
print("YES") if flag else print("NO")
