
import time

a2, b2, c2, d2, f2, g2 = 0, 0, 0, 0, 0, 0
e, h, i, j = 0, 1, 1, 3
e2, h2, i2 = 0, 0, 0
solutions = []
numberOfTrivialSolutions = 0
startTime = time.time()

def testForIntegers(e2, h2, i2):
    # At the end of this function, we set e = 0, so that when this runs for the first time it gets
    # set to the highest of 2/3h2 and 2/3i2

    global numberOfTrivialSolutions

    # Set a, then test to see if a is an integer; then b, c, d, f, g (e is always an integer)
    # Nestled if statements means we don't calculate all of a2, b2, etc at once, which might make it faster
    a2 = 2*e2 - i2
    if ((a2**(1/2.0)).is_integer()):
        b2 = 2*e2 - h2
        if ((b2**(1/2.0)).is_integer()):
            c2 = h2 + i2 - e2
            if ((c2**(1/2.0)).is_integer()):
                d2 = h2 + 2*i2 - 2*e2
                if ((d2**(1/2.0)).is_integer()):
                    f2 = 4*e2 - h2 - 2*i2
                    if ((f2**(1/2.0)).is_integer()):
                        g2 = 3*e2 - h2 - i2
                        if ((g2**(1/2.0)).is_integer()):
                            # Ok, all of them are integers, so we've found a solution
                            if a2 != b2: # This if statement stops solutions where they're all the same number
                                if [a2, b2, c2, d2, e, f2, g2, h2, i2] not in solutions:
                                    # If we haven't already found it, print it and add it to the list of solutions
                                    print ("%s %s %s\n%s %s.0 %s\n%s %s %s\n"
                                        %((a2**(1/2.0)), (b2**(1/2.0)), (c2**(1/2.0)),
                                          (d2**(1/2.0)), (e),           (f2**(1/2.0)),
                                          (g2**(1/2.0)), (h2**(1/2.0)), (i2**(1/2.0))))
                                    solutions.append([a2, b2, c2, d2, e, f2, g2, h2, i2])
                            #else:
                            #    if a2 > numberOfTrivialSolutions:
                            #        numberOfTrivialSolutions += 1

n = 0
m = 0
# start with h and i as 1, increase n
for m in range(0, 900):
    for n in range(0, 900):
        e = 0

        # We'll need these a lot so it's faster to keep them in memory
        # h=m+n, i=m, so h2 = (m+n)**2, i2 = m**2
        # but we don't need to actually assign h and i since that's an extra, unneeded step
        h2, i2 = (m+n)**2, m**2

        while e2 < h2 + i2 and 2*e2 < h2 + 2*i2:

            e2 = e**2
            j = 3*e2

            # These are some of the rules that prevent imaginary solutions
            if j > h2 + i2 and (4/3.0)*j > h2 + 2*i2:
                # Actually test
                testForIntegers(e2, h2, i2)

            # Now make i=m+n, h=m, and square them
            # Since we already have h2=(m+n)**2, it's faster to assign it to i2 instead of recalculating it
            # assuming that assigning values to variables is faster than calculating squares
            i2 = h2
            h2 = m**2

            if j > h2 + i2 and (4/3.0)*j > h2 + 2*i2:
                testForIntegers(e2, h2, i2)

            e += 1

#print " - %s trivial solutions"%(numberOfTrivialSolutions**(1/2.0)) # I have no idea why you have to take the square root of this
                                                                    # also it only works when max n = max m
print " - %s seconds "%(time.time() - startTime)
