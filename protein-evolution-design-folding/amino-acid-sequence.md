# Amino acid sequence

An **amino acid** \(as illustrated in Figure\) is an organic molecule that is made up of a basic **amino** group \(−NH2\), an acidic carboxyl group \(−COOH\), and an organic R group \(or side chain\) that is unique to each **amino acid**. The order of amino acids as they occur in a polypeptide chain, and It is of fundamental importance in determining protein conformation. 

![The 21 proteinogenic amino acids.](../.gitbook/assets/aminoacids.png)

A **multiple sequence alignment** \(**MSA**\), as illustrated in Figure 2, is a sequence alignment of three or more biological sequences, generally protein, DNA, or RNA. Multiple sequence alignments can be useful in many circumstances, e.g., detecting historical and familial relations between sequences of proteins or amino acids and determining certain structures or locations on sequences.

![Figure 2. A multiple sequence alignment of $N$ sequences by $L$ positions. As shown, the lines in dark red stand for the conservation of the amino acids at that position, while the bold lines in orange indicate that the amino acids at position $i$ and $j$ are conserved and coupled.](../.gitbook/assets/msa.png)

### Statistics in aligned sequences

Before one starts to launch Leri, a multiple sequence alignment \(MSA\) is required. Gernerally, Leri does calculations from two sources of MSAs, one is from [HMMER software](http://hmmer.org), and the other one is from [HHblits tool](https://github.com/soedinglab/hh-suite). Firstly, locally install HMMER software and download UniRef database [here](https://www.uniprot.org/downloads). The MSA can be also obtained from the HMMER web-server if you don't want to locally install the software suite. 

Run _jackhmmer_ \(HMMER\) to prepare the MSA by search against the Uniref\*\* database. A simple script that illustrates how to apply the _jackhmmer_ to search a query protein sequence is show as follows,

```bash
$ jackhmmer \
  --notextwi \                                    # Unlimit ASCII text output line width
   -A <USER_DEFINED_FILE.sto> \                   # Save the multiple alignment of hits to file
  --tblout <USER_DEFINED_FILE_tbl.out> \          # Save parseable table of per-sequence hits to file
  --domtblout <USER_DEFINED_FILE_domtbl.out> \    # Save parseable table of per-domain hits to file
   -E 0.01 \                                      # Report sequences <= this E-value threshold in output
  --popen 0.25 \                                  # Gap open probability
  --pextend 0.4 \                                 # Gap extend probability
  --mxfile <DIRECT_TO_BLOSUM62.mat> \             # Read substitution score matrix from file
    <FASTA> \                                      # Query protein sequence
   <DIRECT_TO_Uniref*> \                          # Where to locate the Uniref50, Uniref90, or Uniref100 database
   >/dev/null
```

Run hhblits with default parameters at an E-value threshold 0.001 as shown, 

```bash

```

 When you get the multiple alignment of hits from the _jackhmmer_ and _hhblits_, it is time to launch the Leri to convert the file to the standard FASTA format. The command line that converts \*.sto file to FASTA file is presented here,

```bash
$ leri sequence_converter -jobname <JOB_NAME> -msa <NAME_OF_STO>.sto
```

![FIgure: Similarity between pairwise sequences.](../.gitbook/assets/ww_sequence_similarity.png)

![Figure: Degree of conservation at each independent site.](../.gitbook/assets/ww_site_conservation.png)

Trim aligned sequences according to the query sequence.

```bash
$ leri sequence_trim -jobname <JOB_NAME> -msa <NAME_OF_MSA>_msa.a2m
```

Basic statistics on the aligned sequences,

```bash
$ leri sequence_stats -jobname <JOB_NAME> -msa <NAME_OF_MSA>_msa_trimmed.aln
```



