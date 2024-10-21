# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pch
# Open figure
fig=plt.figure()
ax = fig.add_subplot(1,1,1) 
plt.axis('square')
plt.axis([0,0.7,0,1])
# Add a grey polygon to the plot to form the background shape
ax.add_patch(pch.Polygon([[0,0],[0.7,0],[0.7,0.1],[0.1,0.1],[0.1,0.9]
                          ,[0.6,0.9],[0.6,1],[0,1],[0,0]],facecolor='grey'))
# Add a coral-colored smaller polygon on top of the grey background
ax.add_patch(pch.Polygon([[0.6,0.9],[0.6,0.6],[0.55,0.6],[0.55,0.9],[0.6,0.9]],facecolor='coral'))
ax.text(0.4,0.35,'P',fontsize=80,rotation=-25,fontfamily='serif')
ax.axis('off')
# Show the plot
plt.show()