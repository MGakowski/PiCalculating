from decimal import *

print '[#] The Nilakantha "infinite" series for calculating Pi!'
print "[#] While somewhat more complicated, it converges on pi much quicker than the Leibniz formula. " \
      "Carry this out even a few times and the results get fairly close to pi."

pi = Decimal(3)
loop = int(0)
iterats = int(raw_input("Iterations? "))
inc = int(raw_input("Increments? "))
inccheck = int(loop+inc)
getcontext().prec = int(raw_input("Number of decimal places? "))+1

a = int(2)
b = int(3)
c = int(4)


while loop < iterats:
    if loop == inccheck:
        print str("*Pi is " + str(pi) + " after " + str(loop) + " iterations.")
        inccheck += inc

    abc = Decimal(a * b * c)

    pi += 4 / Decimal(abc)
    a += 2
    b += 2
    c += 2
    loop += 1

    if loop == inccheck:
        print str("*Pi is " + str(pi) + " after " + str(loop) + " iterations.")
        inccheck += inc

    abc = Decimal(a * b * c)

    pi -= 4 / Decimal(abc)
    a += 2
    b += 2
    c += 2
    loop += 1

print str("LIMIT REACHED! Pi is " + str(pi) + " after " + str(loop) + " iterations.")
