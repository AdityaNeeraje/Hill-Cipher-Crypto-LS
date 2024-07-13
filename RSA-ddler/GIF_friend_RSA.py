from sympy.ntheory.factor_ import totient
n=[23270927, 119750403]
e=[65537, 257]
c=[3872687, 58519946]

for i in range(2):
    phi=int(totient(n[i]))
    d=int(pow(e[i],-1,phi))
    print(pow(c[i],d,n[i]))