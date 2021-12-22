def d(n):
    k = str(n)
    for i in k:
        n += int(i)
    return n    

con = list((range(1,10001)))   

for i in range(1,10001):
    if d(i) in con:
        con.remove(d(i))

for m in con:
    print(m)

# con.append(d(x))
# for m in con :
#     if m != x and m == con[-1]:
#         print(x)
#     elif m == x:
#         break
    
       