N,M = map(int,input().split())
st = 1
en = N
s = N*(N+1)//2
for _ in range(M):
    i = int(input())
    if (i>=2 and i<=N-1) or (i==st) or (i==en):
        st,en = en,st
    else:
        s -= en
        en = i
        s += i
    print(s)
