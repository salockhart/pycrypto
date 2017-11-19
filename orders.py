def orders(m):
    orders = []

    for i in range(1, 15):
        orders.append([])
        print "$%d^k \\Mod{%d}$" % (i, m),
        print "$" + str(i) + "^k \\Mod{" + str(m) + "}$",
        for j in range(0, 15):
            orders[i-1].append(pow(i, j, 15))
            print "&", pow(i, j, 15),
        print "\\\\"

    print

    print orders

    for i in range(1, len(orders)+1):
        ord = orders[i-1][1:].index(1) + 1 if 1 in orders[i-1][1:] else 0
        print "\\Order{(%d + %d\\integers)} = %d \\\\" % (i, m, ord)

orders(15)
