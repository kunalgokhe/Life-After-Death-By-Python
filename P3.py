# Import Libraries
import numpy as np
import random
import matplotlib.pyplot as plt
# number of darts
N=1000
# Generate position of darts
x=np.array(random.sample(range(-N,N),N))/N
y=np.array(random.sample(range(-N,N),N))/N
# plots circle
plt.plot(np.cos(2*np.pi*np.linspace(0,1,1000)),np.sin(2*np.pi*np.linspace(0,1,1000)),'k',linewidth=1)
# Compute distance from center
d=np.sqrt(x**2+y**2)
# Plot darts which is plotted inside circle as green 
plt.scatter(x[d>1],y[d>1],marker='.',c='r',s=1)
plt.scatter(x[d<1],y[d<1],marker='.',c='g',s=1)
plt.axis([-1,1,-1,1])
plt.axis('square')
# Show the plot
plt.show()
print('Approximate values of pi is ',4*sum(d<1)/N)

# Simulate for multiple replications
val=[]
for i in range(1000):
    # Generate position of darts
    x=np.array(random.sample(range(-N,N),N))/N
    y=np.array(random.sample(range(-N,N),N))/N
    # Compute distance from center
    d=np.sqrt(x**2+y**2)
    val.append(4*sum(d<1)/N)
# Plot histogram    
plt.hist(val,density=True)
# Plot true values of pi
plt.plot([np.pi,np.pi],[0,10],'--')
plt.legend(['True value'])
# Show the plot
plt.show()