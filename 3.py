import cplex
import numpy as np

# Load model( file .mps import from AMPL)
c = cplex.Cplex("tsp.mps")

Tableau = np.zeros((14,132));

# Solve the problem (iter by iter)
c.parameters.simplex.limits.iterations.set(1)
c.parameters.lpmethod.set(c.parameters.lpmethod.values.primal)
while c.solution.get_status() != c.solution.status.optimal:
    c.solve()
    
cont = 0;
# Final Simplex Tableau
for tableau_row in c.solution.advanced.binvarow():
    Tableau[cont,:] = tableau_row;
    cont = cont+1; 

# Basis info
c.solution.basis.write("basis.mps")

#Solution
SOL = c.solution.get_values();



