import numpy as np

# Save results in file test.txt
a = open('test.txt', 'w')
# NN heuristic for each initial node
for k in np.arange(0,12,1):

    # mark used node
    nodes = np.zeros(12);
    nodes[k] = 1;
    # tour
    tour = [k];
    # Initialize
    ok = len(np.where(nodes==0)[0]);
    i0 = k;
    while ok > 0:
        pos = np.where(nodes==0)[0];
        # Find nearest neighbor
        i1 = pos[np.where(D[pos,i0]== min(D[pos,i0]))[0]];
        # Add nearest neighbor
        tour.append(i1[0])
        # Update cost
        cost[k] = cost[k] + D[i0,i1];
        # mark used node
        nodes[i1] = 1;
        # Updates
        i0 = i1;
        ok = len(np.where(nodes==0)[0]);
    
    # Add final edge to close tour
    cost[k] = cost[k]+ D[i1,k];   
    tour.append(k)
    # Save results
    a.write('NN(%s'%k+'):\n'+'%s' % tour +' -- z* = %s\n' % cost[k]) 
    # 2-Interchange heuristic for each NN tour solution
    for i in np.arange(0,10,1):
        
        for j in np.arange(i+2,12,1):
            d1 = D[tour[i],tour[i+1]] + D[tour[j],tour[j+1]];
            d2 = D[tour[i],tour[j]] + D[tour[i+1],tour[j+1]];
            
            # Do swap if interchange improves upper bound 
            if d2 < d1:
                tour[i+1:j+1] = np.flip(tour[i+1:j+1])
                cost[k] = cost[k]-d1+d2;
                a.write('%s' % tour+' -- z* = %s\n' % cost[k])
a.close()




