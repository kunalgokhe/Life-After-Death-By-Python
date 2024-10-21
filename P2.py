# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
# Define function
n = lambda m: 108/m
def comb(k):
    return k*(k-1)/2
f = lambda m: comb(n(m))+comb(m)-102
# Solve using fsolce
m=fsolve(f,100)
n=n(m)
# Display results
print(f'n={round(n[0])} and m={round(m[0])}')