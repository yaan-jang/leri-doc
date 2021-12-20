---
description: >-
  Residue communities are evolutionary signatures  that are inferred from
  protein evolution.
---

# Residue communities

In evolutionary coupling analysis (ECA) approach, we focus on the detections of coupling amino acids at conserved positions using a relative entropy as shown in Eq. (1) to filter interactions at weak- or non-conservation sites. The specified network of interactions between amino acids, as illustrated in Figure 2, estimated from sequence alignment can be a trade-off between consensus and couplings, which also tests our understanding of that proteins have evolved for function but not stability.

![](../.gitbook/assets/evolutionary\_coupled\_block.png)

### Pairwise coupings and evolutionary block

For example, we run `leri` on a ww-domain protein after get the aligned sequences by `jackhmmer`.&#x20;

```bash
$ leri sequence_eca -msa <multiple_sequence_alignment>
```

![Figure: From (a) evolutionary couplings to (b) amino acid blocks (smaller is at top left, and bigger is at bottom right) inferred from protein family PF00014, and (c) mapping to the tertiary structure (PDB ID: 1AAP).](../.gitbook/assets/coupling-block.png)
