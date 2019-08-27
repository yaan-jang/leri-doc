# Evolutionary couplings of amino acids

In evolutionary coupling analysis \(ECA\) approach, we focus on the detections of coupling amino acids at conserved positions using a relative entropy as shown in Eq. \(1\) to filter interactions at weak- or non-conservation sites. The specified network of interactions between amino acids, as illustrated in Figure 2, estimated from sequence alignment can be a trade-off between consensus and couplings, which also tests our understanding of that proteins have evolved for function but not stability.

![](../.gitbook/assets/evolutionary_coupled_block.png)

### Pairwise coupings and evolutionary block

For example, we run `leri` on a ww-domain protein after get the aligned sequences by `jackhmmer`. 

```bash
$ leri sequence_coupling -msa <multiple_sequence_alignment>
```

![Figure: \(a\) Evolutionary couplings computed from the MSA of the ww-domain protein, and \(b\) the pairwise interactions between the amino acids in the coupled &apos;blocks&apos;. ](../.gitbook/assets/coupling-block.png)

