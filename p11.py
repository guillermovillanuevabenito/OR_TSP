import cplex
import numpy as np

# Load model( file .mps)
c = cplex.Cplex()
out = c.set_results_stream(None)
out = c.set_log_stream(None)
c.read("tsp.mps")

#Solve problem
c.solve()

# Compute Simplex Tableau
Tableau = np.zeros((14,132));
cont = 0;
for tableau_row in c.solution.advanced.binvarow():
    Tableau[cont,:] = tableau_row;
    cont = cont+1; 

# Basis info
c.solution.basis.write("basis.mps")

#Solution
SOL = c.solution.get_values();




