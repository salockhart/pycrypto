import sys

g = int(sys.argv[1])
p = int(sys.argv[2])

for k in range(0, p):
    if k != 0 and pow(g, k, p) == 1:
        print "Order =", k
        break