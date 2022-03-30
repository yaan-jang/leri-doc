# Ramachandran map

### Generation of statistical potential

```
leri rama_map \
-jobname rama_potential \
-type 0 \
-alpha 5.0 \                  # bin size for rama map
-index list_proteins \        # index of all protein IDs
-dirt /path_to_STRIDE_ouput/ 
```

### Rama map for a single protein

```
leri rama_map \
-jobname rama_map \
-type 1 \
-fastx XXXXX.fasta \
-alpha 5.0 \                 # bin size for rama map
-index sec_strucure \        # secondary structure (initially, all 'A')
-dirt /path_to_STRIDE_ouput/ \
-hlog                        # local visualization
```
