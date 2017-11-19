import sys
import random
import extended_euclid

n = int(sys.argv[1])

print 'n =', n


def composite():
    print 'composite'
    sys.exit(0)


def prime():
    print 'prime'
    sys.exit(0)

if n % 2 == 0:
    composite()

s = 0

while (n - 1) % pow(2, s + 1) == 0:
    s = s + 1

print 's =', s

d = (n - 1) / pow(2, s)

print 'd =', d

for i in range(1, 10):
    a = random.randint(2, n - 1)
    print 'random =', a
    gcd = extended_euclid.egcd(a, n)[0]
    if gcd > 1:
        composite()
    found = False
    if pow(a, d, n) == 1:
        found = True
    for r in range(0, s):
        if pow(a, pow(2, r) * d, n) == n - 1:
            found = True
    if not found:
        composite()

prime()
