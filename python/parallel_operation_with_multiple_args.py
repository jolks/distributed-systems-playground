#!/usr/bin/env python

# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool
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
p = ThreadPool() 

# Regardless of input type, output will be list type
print p.map(f_star, [[1, 2, 3], [3, 4, 5], [5, 6, 7]]) # list of lists input
print p.map(f_star, ((1, 2, 3), (3, 4, 5), (5, 6, 7))) # tuple of tuples input

# Close the pool. No task is allowed anymore.  
p.close()

# Wait for the workers to exit.
p.join()


