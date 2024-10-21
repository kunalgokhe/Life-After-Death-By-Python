# Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# Define Parameters
lmda=1
Ne=50
Ng=2*Ne

# Plot 2D snapshot
# Generate y-direction data
ye=np.random.exponential(lmda,Ne)
yg=np.random.exponential(lmda,Ng)
# Generate x-direction data
x=np.random.uniform(0,1,3*Ne)
# Plot data
plt.scatter(x[0:Ne],ye,color='red')
plt.scatter(x[Ne:],yg,color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['e','g'])
# Show plot
plt.show()

# Define Parameters
lmda=1
Ne=10
Ng=2*Ne
# Plot 3D snapshot
# Generate x and y-direction data
x=np.random.uniform(0,1,[3*Ne,3*Ne])
y=np.random.uniform(0,1,[3*Ne,3*Ne])
# Generate z-direction data
ze=np.random.exponential(lmda,[Ne,Ne])
zg=np.random.exponential(lmda,[Ng,Ng])
# Plot data
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.scatter(x[0:Ne,0:Ne],y[0:Ne,0:Ne],ze,color='red')
ax.scatter(x[Ne:,Ne:],y[Ne:,Ne:],zg,color='blue')
ax.grid(False)
plt.xlabel('x')
plt.ylabel('y')
ax.set_zlabel('z')
plt.legend(['e','g'])
# Show plot
plt.show()