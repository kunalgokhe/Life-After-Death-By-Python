# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# Fixed point iteration Function
def fixedPoint(f,xold,tol,maxIter):
    itr=0
    x=[]
    while True:
        x.append(xold)
        xnew=f(xold)
        if abs(xnew-xold)<tol or itr>maxIter:
            break
        xold=xnew
        itr+=1
    return xnew,itr,x

# Babylonian Method
# Define function
S=125348  
f=lambda x: (x+S/x)/2
# Define parameters
xold=1000
maxIter=100
tol=1e-6
# Compute root
xnew,itr,x=fixedPoint(f,xold,tol,maxIter)
# Print and plot solution
print(f'Using babylonian Method sqrt({S}) is {xnew}')
plt.plot(x)

# Indian Method
# Define function
S=125348  
a=lambda x:(S-x**2)/(2*x)
f1=lambda x: x+a(x)-0.5*a(x)**2/(x+a(x))
# Define Parameters
xold=1000
maxIter=100
tol=1e-6
# Compute root
xnew,itr,x=fixedPoint(f1,xold,tol,maxIter)
# Print and plot solution
print(f'Using Indian Method sqrt({S}) is {xnew}')
plt.plot(x)
plt.xlabel('No. of Iterations')
plt.ylabel(r'$\sqrt{S}$')
plt.legend(['Babylonian','Indian'])
plt.title(r'$\sqrt{S}$  Vs No. of Iterations')
# Show plot
plt.show()