# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Compute root Fucntion
def computeRoot(m):
    # Create Hp Matrix
    A=np.diag([1]*(m-1),-1)
    # Number of possible combination of coefficients
    n=2**(m+1)
    x=[]
    y=[]
    # Compute root for each coefficients
    for i in range(n):
        # Create Hp matrix
        p=np.array([int(i)*2-1 for i in list('{:0{m}b}'.format(i,m=m+1))])
        b=p[:0:-1]/p[-1]
        A[0,:]=b
        # Compute eigenvalue (roots)
        eigval=np.linalg.eig(A).eigenvalues
        # Store real and imaginary roots
        x.append(np.real(eigval))
        y.append(np.imag(eigval))
    return np.array(x),np.array(y)

# Open figure
fig=plt.figure()
# Compute roots for degree 1 to 11
for m in range(1,12):
    x,y=computeRoot(m)
    # Plot roots
    plt.scatter([x,-x],[y,y],marker='.',s=0.1)
# Plot Axis and Circles
plt.plot([0,0],[-2,2],color='grey',linewidth=0.5)
plt.plot([-2,2],[0,0],color='grey',linewidth=0.5)
theta=np.linspace(0,2*np.pi,1001)
plt.plot(1.9*np.cos(theta),1.9*np.sin(theta),color='grey',linewidth=0.5)
plt.axis('square')
plt.axis([-2,2,-2,2])
plt.axis('off')
plt.show()
