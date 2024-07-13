import sympy
import numpy

d=77266263685307006230322907286315353524856777913832852852497884154975370477569
n=115792089237316195423570985008687907853269984665640564039457584007913129639937
tot= sympy.totient(n)
e_square=sympy.mod_inverse(d,tot)

# print(e_square)
e= int(numpy.sqrt(e_square))
# print(numpy.sqrt(e_square))
print(sympy.mod_inverse(e, tot))