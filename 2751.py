from sys import stdin

N = int(stdin.readline())
L1 = [0]*N

for i in range(N):
    L1[i] = int(stdin.readline())    
    
R = set(L1)
R = sorted(R)
       
s = ""
for x in R:
    s += (str(x) + '\n')

print(s)