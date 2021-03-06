#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# Converted to Python 3 from Python 2
# $ 2to3 -w parallel_operation_with_multiple_args.py 

from multiprocessing import Pool
import math

def f(x, y, z):
    # (x + 2y)^z
    return math.pow(x + 2*y, z)

# In Python 3.3, can use starmap() method instead
def f_star(multiple_args):
    # Changes e.g. f([1,2,3]) to f(1, 2, 3)
    return f(*multiple_args)

# Set no. of workers in the pool. 
# If the argument is not set, it defaults to machine no. of cores.
p = Pool(4) # Initialize 4 parallel processes which can be seen using top command   

# Regardless of input type, output will be list type
print(p.map(f_star, [[1, 2, 3], [3, 4, 5], [5, 6, 7]])) # list of lists input
print(p.map(f_star, ((1, 2, 3), (3, 4, 5), (5, 6, 7)))) # tuple of tuples input

# Close the pool. No task is allowed anymore.  
p.close()

# Wait for the workers to exit.
p.join()


