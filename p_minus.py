import sys
import math
import extended_euclid

def factor(n):
    B = 100
    Bfactorial = math.factorial(B)
    a = 2

    factorial_exponent = pow(a, Bfactorial, n)

    p = extended_euclid.egcd(factorial_exponent - 1, n)[0]
    q = int(n // p)
    return (p, q)

n = int(sys.argv[1])
p, q = factor(n)
print("p =", p)
print("q =", q)
assert n == (p * q)
