import sympy
import numpy

d=56758248688344445618535855545843339303
n=69203410113561398433978337198079999737
tot= sympy.totient(n)
e_cube=sympy.mod_inverse(d,tot)

print(e_cube, numpy.cbrt(e_cube))
e= int(numpy.cbrt(e_cube))
assert 524287*524287*524287==e_cube
# print(numpy.sqrt(e_square))
print(sympy.mod_inverse(524287, tot))