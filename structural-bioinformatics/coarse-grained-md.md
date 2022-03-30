# Coarse-grained MD

### Run Modyfing

#### Predict torsion angles&#x20;

```
# index, phi, psi
1,360.00,144.52
2,-68.89,146.90
3,-67.84,167.71
4,-48.66,126.77
5,89.47,-16.22
6,-82.96,141.75
7,-146.98,152.93
8,-89.62,129.75
9,-131.53,175.67
10,-117.11,126.54
```

#### Predict residue-contacts

```
# index 1, index 2, distance/couplings
1,2,1,3.78394
1,3,1,6.39359
1,32,1,7.11550
1,33,1,7.27484
2,1,1,3.78394
2,3,1,3.83337
2,4,1,6.70233
2,6,1,5.72527
2,7,1,6.95126
2,31,1,6.55447
2,32,1,5.79209
3,1,1,6.39359
3,2,1,3.83337
3,4,1,3.83061
```

#### Configuration

```
# Initial structure 
pdb = /PATH_TO/ww.pdb

# Neighbor-dependent Ramachandran Distributions 
ndrd = /PATH_TO/NDRD_TCB.par.bz2

# Backbone-dependent rotamer library 
dirt_bdrl = /PATH_TO/backbone_dependent/

# bdrl = /PATH_TO/backbone_dependent_com.h5
# radial-MJ-1996 potential 
# rmjp = /PATH_TO/radial-MJ-1996.h5
# rmjp = /PATH_TO/radial-MJ-1996

# Constraint for torsion angles 
# [a-20, a+20] 
phi_upper_bias = 20 
psi_upper_bias = 20 
phi_lower_bias = -20 
psi_lower_bias = -20
phsi = /PATH_TO/ww.phsi

% H-bond 
hbond_scale = -4.0

% Contact maps 
% the index for the first residue must start from 1 
% The higher the value of dist_threshold, the stronger the constraint is dist_threshold = 12.5 
% dist_centroid is for r0 
dist_centroid = 7.5 
dist_space_cutoff = 6 
dist_scale = 5.0 
dist_energy_wgt_ = -1.5 
% Accept format 
% index 1, index 2, energy 
% index 1, index 2, energy, r0 
% index 1, index 2, energy, r0, scale
dist_map = /PATH_TO/ww_dist_map.csv
```



#### Predict folding pathways and 3D structure

```
leri modyfing \
-fastx ww.fasta \  
-cfg ww.cfg \
-max_iter 2000 \
-intv 1 \
-temperature 1.0 \
-threads 1 \
-output <DIRECTORY>
```
