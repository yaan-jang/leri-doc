# Multiple sequence alignment

### Generate MSA from different databases

#### _jackhmmer_ on [UniRef90](https://www.uniprot.org/help/uniref)/[MGnify](https://www.ebi.ac.uk/metagenomics/)

```
jackhmmer \
-o /dev/null \
--cpu 16 \
--noali \
--F1 0.0005 \
--F2 5e-05 \
--F3 5e-07 \
--incE 0.0001 \
-E 0.0001 \
-N 1 \
-A output.sto \
XX.fasta \
uniref90.fasta
```

#### hhblits on [Uniclust30](https://uniclust.mmseqs.com)/[BFD](https://bfd.mmseqs.com) databases

```
hhblits \
-i XX.fasta \
-cpu 16 \
-oa3m output.a3m \
-o /dev/null \
-n 3 \
-e 0.001 \
-maxseq 1000000 \
-realign_max 100000 \
-maxfilt 100000 \
-min_prefilter_hits 1000 \
-d UniRef30_2020_06
// using <-d> to add more databas
```

### Align between pairwise sequences

Provided two or more than two biological sequences, we leverage `leri` to align them using Needleman-Wunsch algorithm.  `-jobname` indicates results of the job will be output in the folder, `-msa` is to load the sequences where you have,`-print` is to show the information of each alignment`.`

```
leri sequence_align \
-jobname <JOB_NAME> \
-print \
-msa leri-example/msa/<TARGET_MULTIPLE_SEQUNECS>.a3m
```
