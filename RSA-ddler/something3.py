import sympy
import numpy

# Turns out e^2 mod n is simply e^2, since e^2 is less than n. Hence, the actual d to use is the modinverse of the sqrt of the e^2, which we can find by using the fact that e^2 * d = 1 mod tot(n). 
d=77266263685307006230322907286315353524856777913832852852497884154975370477569
n=115792089237316195423570985008687907853269984665640564039457584007913129639937
tot= sympy.totient(n)
e_square=sympy.mod_inverse(d,tot)

# print(e_square)
e= int(numpy.sqrt(e_square))
# print(numpy.sqrt(e_square))
print(sympy.mod_inverse(e, tot))
