import sys
import math

k = int(sys.argv[1]) # persons
n = int(sys.argv[2]) # birthdays

print 'k =', k
print 'n =', n

q = math.exp( -(k * (k-1)) / (2.0*n) )
p = 1-q

print 'q =', q
print 'p =', p
