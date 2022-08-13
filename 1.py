import numpy as np
import matplotlib.pyplot as plt
import networkx
import random as rn

# Create random coordinates
A = np.random.random((12,2))
x = A[:,0];
y = A[:,1];

# Compute cost matrix C (distance matrix)
C = np.zeros((12,12));
for i in range(len(x)):
    for j in range(len(y)):
        C[i,j] = np.round(np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2),3)

# Create complete graph with n = 12
G = networkx.complete_graph(12)

# Set the position of nodes
pos = networkx.spring_layout(G)
for i in range(12):
  pos[i] = A[i,:]

# Plot the graph
fig, ax = plt.subplots(figsize=(10, 10))
networkx.draw(G, pos, with_labels=True,font_color="whitesmoke",ax=ax,node_size = 1000,font_weight ='bold',font_size = 20)
limits=plt.axis('on') # turns on axis
plt.ylabel('y',fontsize=20)
plt.xlabel('x',fontsize=20)
ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True,labelsize=18)


