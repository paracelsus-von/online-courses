# Uses python2
# There are two ways of running this program:
# 1. Run
#     python APlusB.py
# then enter two numbers and press ctrl-d
# 2. Save two numbers to a file -- say, dataset.txt.
# Then run
#     python APlusB.py < dataset.txt

import sys

input1 = sys.stdin.read()
tokens = input1.split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)
