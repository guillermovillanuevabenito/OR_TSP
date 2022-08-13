# parameters
param n;
set nodes ordered := {1..n};
set edges := {i in nodes, j in nodes};

set nodes1 ordered := {3,4,11};
set edges1 := {i in nodes1, j in nodes1};

param c {(i,j) in edges};
var X {(i,j) in edges} >=0, <=1;

#Objective function
minimize fobj : sum {(i,j) in edges} (c[i,j]*X[i,j]);

#Constraints
subject to cc1 {i in nodes}: sum{(i,j) in edges: i < j} (X[i,j]) + sum{(i,j) in edges: j < i} (X[j,i])= 2; 
subject to cc2: sum{(i,j) in edges1:i < j} (X[i,j]) <= 2; 
subject to cc3: X[2,6]+X[2,10]+X[6,10]+X[2,7]+X[6,7]+X[10,12] <= 4; 
subject to cc4: X[5,8] - X[1,4]-X[1,11]-X[2,4]-X[2,11]-X[4,6]-X[4,7]-X[4,9]-X[4,10]-X[4,12]-X[6,11]-X[7,11]-X[9,11]-X[10,11]-X[11,12] <= 0; 
