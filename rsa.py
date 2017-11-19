import sys
import extended_euclid

n = int(sys.argv[1])
e = int(sys.argv[2])
c = int(sys.argv[3])

print('n =', n)
print('e =', e)
print('c =', c)

def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def factor(n):
    a = isqrt(n)
    b2 = a * a - n
    b = isqrt(n)
    while b * b != b2:
        a = a + 1
        b2 = a * a - n
        b = isqrt(b2)
    p = a + b
    q = a - b
    assert n == p * q
    return (p, q)

def phi(factors):
    return (factors[0] - 1) * (factors[1] - 1)

factors = factor(n)
print('n =', " * ".join(str(factor) for factor in factors))

phin = phi(factors)
print('phi(n) =', phin)

extended = extended_euclid.egcd(e, phin)
d = int(extended[1]) % phin
print('d =', d)

m = pow(c, d, n)
print('m =', m)

assert pow(m, e, n) == c
