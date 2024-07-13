import sympy as sp

# Thid code finds the value of d for the values which are indexed 1 modulo 4. This is simply a case of straightforward RSA
large_prime = 124620366781718784065835044608106590434820374651678805754818788883289666801188210855036039570272508747509864768438458621054865537970253930571891217684318286362846948405301614416430468066875699415246993185704183030512549594371372159029236099

tot=large_prime-1
if (tot%3==0):
    print("Divisible")
    exit()
mod_inverse = sp.mod_inverse(3, sp.totient(large_prime))

print(f"The modular inverse of 3 modulo {large_prime} is: {mod_inverse}")
