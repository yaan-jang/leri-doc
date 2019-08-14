# Usage

```text
leri:  usage command line
 leri <command> <args>
 
 These are common Ler commands used in various situations:
 
 get leri and system info. (see also: leri help tutorial)
  about                -about leri
  usage                -usage of leri
 
 work on the omics (see also: leri help metaomics)
  sff2fastq            -convert an SFF file from the 454 genome sequencer
                        to FASTQ including the sequences and quality scores
  base_call            -Base calling
  atgc_stats           -Statistics of FASTQ sequence
  atgc_quality         -Quality control
  atgc_correct         -Correct errors in sequencing data
  atgc_assembly        -sequence assembly by de Bruijn graph or ant colony optimization
  read_filter          -Filter reads with low quality
  kmer_counter         -count kmer
  kmer_generator       -generate kmers
 
 work on the proteomics (see also: leri help proteomics)
  sequence_converter   -convert the ouput of Jackhmmer to fasta
  sequence_mix         -pairwise-mixture protein sequences (particular for GPCR-G proteins)
  sequence_trim        -trim a multiple protein sequence alignment
  sequence_stats       -statistical analysis on a protein mutiple sequence alignment
  sequence_coupling    -coupled relationship betwen pairwise protein residues and functional sectors
  sequence_eca         -infer coupled blocks of protein residues at conserved sites
  sequence_energy      -calculate energy for a protein sequence or multiple sequences
  sequence_design      -design a protein sequence
  sequence_ddg         -infer protein stability (ddG = dG_wt - dG_mutant)
  point_mutation       -point mutation for a given protein sequence
  residue_contact      -estimate contacts between pairwise residues from protein MSA
  selectivity_sector   -detect selectivity sectors of determinants in GPCR-G proteins
 
 work on protein folding
  pdb_parser           -parser a PDB file and write it out in simplified PDB format and/or FASTA sequence file
  fasta2pdb            -convert protien amino acid sequence into its extended structure
  fold_protein         -predict tertiary structure
  protein_folding      -predict folding pathways & tertiary structure
  calc_contact         -calculate residue contacts from a give PDB file
 
 work on statistics (see also: leri help statistics)
  stats_ica            -independent component analysis on a given matrix
  stats_pearson        -Pearson correlation
  stats_tsne           -t-distributed stochastic neighbor embedding (t-SNE) method
 
 work on optimization tools (see also: leri help optimization)
  opt_chpso            -the convergent heterogeneous particle swarm optimizer
  opt_jde              -the differential evolution optimizer
 
 work on sampling (see also: leri help sampling)
  nested_sampler       -nested sampler
 
 work on machine learning (see also: leri help learning)
  senet                -sequentially evolving neural network
  optifel              -evolving fuzzy modeling approach
  phsior               -protein torsion angle predictor based on CNN deep network
```

