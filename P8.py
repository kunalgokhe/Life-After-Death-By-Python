# Import Libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Kaprekar function
def kaprekar(a):
    A=a
    itr=1
    while True:
        a=''.join(sorted(list('{:04d}'.format(a)),reverse=True))
        n1=int(a)
        n2=int(a[::-1])
        n=max(n1,n2)-min(n1,n2)
        if int(n)==6174 or itr>8:
            if itr>7:
                itr=0
            break
        a=n
        itr+=1
    return itr

# Define n
n=list(range(0,10000))
# Compute kaprekar values
val=[kaprekar(i) for i in n]
# Compute x and y positions
y=np.mod(range(10000),100)
x=np.floor(np.array(list(range(10000))))
# Create matrix
m=np.zeros([100,100])
n=0
for i in range(100):
    for j in range(100):
        m[int(x[i]),int(y[j])]=val[n]
        n+=1
# Define color for iteration number
colors = {
    0: (1, 1, 1),          
    1: (1, 6/7, 0),        
    2: (2/7, 1, 0),        
    3: (0, 1, 4/7),        
    4: (0, 4/7, 1),        
    5: (2/7, 0, 1),        
    6: (1, 0, 6/7),        
    7: (1, 0, 0)          
}
# Create custom map
map = [(i/7, colors[i]) for i in range(8)]
cmap = LinearSegmentedColormap.from_list("custom_cmap", map)
# Show Image
plt.imshow(m,origin='lower',cmap = cmap)
plt.ylabel(r'$ n~mod~\sqrt{10^4} $',color='grey')
plt.xlabel(r'$ n~div~\sqrt{10^4} $',color='grey')
plt.title(r'$6174$',color='grey',size=8)
plt.tight_layout(pad=0.1)
ax=plt.gca()
# Grey all the axis
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.spines['top'].set_color('grey')
ax.spines['right'].set_color('grey')
ax.tick_params(axis='x',colors='grey')
ax.tick_params(axis='y',colors='grey')
# Show Plot
plt.show()

## Extra for Odd and Even Number of Iterations
# Create matrix
m=np.zeros([100,100])
n=0
for i in range(100):
    for j in range(100):
        if np.mod(val[n],2)==0:
            m[int(x[i]),int(y[j])]=1
        n+=1
# Show Image
plt.imshow(m,origin='lower',cmap = 'winter')
plt.ylabel(r'$ n~mod~\sqrt{10^4} $',color='grey')
plt.xlabel(r'$ n~div~\sqrt{10^4} $',color='grey')
plt.title(r'$6174$',color='grey',size=8)
plt.tight_layout(pad=0.1)
ax=plt.gca()
# Grey all the axis
ax.spines['bottom'].set_color('grey')
ax.spines['left'].set_color('grey')
ax.spines['top'].set_color('grey')
ax.spines['right'].set_color('grey')
ax.tick_params(axis='x',colors='grey')
ax.tick_params(axis='y',colors='grey')
# Show Plot
plt.show()