N = int(input())
L1 = []

while True:
    try:
        x = int(input())
        
        if -1000 <= x <=1000:
            L1.append(x)
            
        R = set(L1)
        R = sorted(R)
   
        if len(L1) == N:
            break
        
    except ValueError:
        continue

for x in R:
    print(x)