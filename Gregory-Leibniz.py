from decimal import *

print '[#] The Gregory-Leibniz "infinite" series for calculating Pi!'
print "[#] Though not very efficient, it will get closer and closer to pi with every iteration, accurately producing " \
      "pi to five decimal places with 500,000 iterations."

pi = Decimal(0)
odd = Decimal(1)
loop = int(0)
iterats = int(raw_input("Iterations? "))
inc = int(raw_input("Increments? "))
inccheck = int(loop+inc)
getcontext().prec = int(raw_input("Number of decimal places? "))+1


while loop < iterats:

    if loop == inccheck:
        print str("*Pi is " + str(pi) + " after " + str(loop) + " iterations.")
        inccheck += inc

    pi += 4 / odd
    odd += 2
    loop += 1

    if loop == inccheck:
        print str("*Pi is " + str(pi) + " after " + str(loop) + " iterations.")
        inccheck += inc

    pi -= 4 / odd
    odd += 2
    loop += 1

print str("LIMIT REACHED! Pi is " + str(pi) + " after " + str(loop) + " iterations.")
