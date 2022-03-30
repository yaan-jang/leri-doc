---
description: >-
  Residue communities are evolutionary signatures  that are inferred from
  protein evolution.
---

# Residue communities

In evolutionary coupling analysis (ECA) approach, we focus on the detections of coupling amino acids at conserved positions using a relative entropy as shown in Eq. (1) to filter interactions at weak- or non-conservation sites. The specified network of interactions between amino acids, as illustrated in Figure 2, estimated from sequence alignment can be a trade-off between consensus and couplings, which also tests our understanding of that proteins have evolved for function but not stability.

![](../.gitbook/assets/evolutionary\_coupled\_block.png)

### Pairwise couplings and evolutionary block

For example, we run `leri` on a protein (1AAP) from the aligned sequences from Pfam`[ref]`.&#x20;

```bash
$ leri sequence_eca \
-jobname pf00014 \
-threads 4 \
-max_iter 2000 \ 
-threshold -1.0 \    # no threshold for selection
-gap_frac 1.0 \      # gaps in a sequence 
-site_gap_frac 1.0   # gaps in a site of the given MSA
-offset 0            # starting index for output results
-msa <path_to_multiple_sequence_alignment> \
-hlog                # local visualization
```

![Figure: From (a) evolutionary couplings to (b) amino acid blocks (smaller is at top left, and bigger is at bottom right) inferred from protein family PF00014, and (c) mapping to the tertiary structure (PDB ID: 1AAP).](../.gitbook/assets/coupling-block.png)
