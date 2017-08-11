import random

# Params

arraylimit = 10
intlimit = 1000000

def pairwisefast(sample):
    sample.sort()
    return(sample[-1] * sample[-2])

def pairwise(sample):
    x = max(sample)
    sample.remove(x)
    y = max(sample)
    return(x*y)

a = 0
b = 0

while a == b:
    print "\nOK\n\n------------\n\n"
    n = random.randint(2,arraylimit)
    sample = []
    for x in xrange(n):
        sample.append(random.randint(1,intlimit))
    a = pairwisefast(sample)
    b = pairwise(sample)
    print sample
    print a
    print b

print pairwisefast(sample[i])

print pairwise(sample[i])
