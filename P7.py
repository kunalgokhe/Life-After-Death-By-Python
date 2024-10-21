# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# Greatest Common Divisor Function
def GCD(a,b):
    itr=0
    while b!=0:
        r=np.mod(a,b)
        a,b=b,r
        itr+=1
    return a,itr
vf=np.vectorize(GCD)

## Coprime pair    
N=100
a,b=np.meshgrid(np.linspace(0,N,N+1),np.linspace(0,N,N+1))
# Compute GCD
coprime,itr=vf(a,b)
# Plot coprime==1
plt.imshow(coprime==1,cmap='winter')
plt.colorbar()
plt.xlabel('a')
plt.ylabel('y')
plt.title('Coprime')
plt.show()

## No. of iteration for each pair(a,b)
N=500
a,b=np.meshgrid(np.linspace(0,N,N+1),np.linspace(0,N,N+1))
# Compute GCD
coprime,itr=vf(a,b)
# plot no. of iterations
map=plt.cm.get_cmap('jet') 
plt.imshow(itr,cmap=map.reversed(),origin='lower')
plt.colorbar()
plt.xlabel('a')
plt.ylabel('y')
plt.title('No. of Steps')
plt.show()

# Convergence Analysis for coprime fraction
frac=[]
for N in range(1,501,10):
    a,b=np.meshgrid(np.linspace(0,N,N+1),np.linspace(0,N,N+1))
    coprime,itr=vf(a,b)
    frac.append(sum(sum(coprime==1))/(N*N))
# Plot coprime fraction
plt.plot(range(1,501,10),frac,linewidth=1)
plt.plot(range(1,501,10),[6/np.pi**2]*50,'--',linewidth=1)
plt.xlabel('n')
plt.ylabel('Coprime Fraction')
plt.title('Coprime fraction Vs n')
plt.legend(['Coprime',r'$6/\pi^2$'])
plt.show()
