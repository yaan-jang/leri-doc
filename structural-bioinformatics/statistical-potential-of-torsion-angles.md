# Statistical potential of torsion angles

Generate the potential 

```text
leri rama_map \
-type 0 \         # generate the potentail from PDBs
-alpha <INT> \    # degree of bin size 
-dirt  <STRING> \ # that contains the potenial file
-index <STRING>   # list of the PDBs
```

Generate the Ramachandran map for a sequence

```text
leri rama_map \
-type 1 \          # for a specific sequence
-fastx <STRING> \  # query sequence
-dirt  <STRING> \  # that contains the potenial file
-index <STRING> \  # secondary structure
-alpha <INT>       # degree of each bin size 
```

