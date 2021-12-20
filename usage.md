# Usage

### Generating MSA

#### Generate an MSA by _`hhblits`_

```bash
# Use HHBLITS to generate MSA
tmp_dirt=<temporary directory>
n_threads=4 # number of threads
id=1A2YA # PDB ID and chain of an example
hhblits \
-v 0 \
-d /<directory_to_the_database>/uniclust/UniRef30_2020_03 \
-cpu ${n_threads} \
-n 5 \
-E 0.001 \
-o ${tmp_dirt}/${id}.hhr \
-opsi ${tmp_dirt}/${id}_psiblast.aln \
-i /<directory_to_the_FASTA>/${id}.fasta
```

#### Generate an MSA by _`jackhmmer`_

```bash
jackhmmer \
 --notextw \
 --cpu ${n_threads}  \
 -A ${tmp_dirt}/${id}.sto \
 --tblout ${tmp_dirt}/${id}_tbl.out \
 --domtblout ${tmp_dirt}/${id}_domtbl.out  \
 -E 0.01 \
 --popen 0.25 \
 --pextend 0.4 \
 ${seq_dirt}/${id}.fasta \
 /<directory_to_the_database>/uniref100.fasta \
 
# Convert format 
leri sequence_converter \
 -jobname ${id} \
 -type 1 \
 -msa ${tmp_dirt}/${id}.sto \
 -threads ${n_threads} \
 -output ${out_dirt}
```

### Usage of `leri`

```
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

Example pipeline

```bash
#!/bin/bash

jackhmmer=/usr/local/bin/jackhmmer
usrname=`whoami`
home_dirt=/home/${usrname}
dirt=${home_dirt}/leri-analytics
#lib_dirt=${dirt}/leri-lib
leri=${dirt}/leri-build/tool/leri

data_idx=90
database=${home_dirt}/.data/uniref${data_idx}.fasta

out_dirt=${dirt}/leri-output


#bin_dir=${dirt}/leri-bin
#srp_dir=${dirt}/leri-scripts
exp_dirt=${dirt}/leri-example
seq_dirt=${exp_dirt}/fasta


if [ $# -ne 1 ]; then
  echo "Usage: $0 <protein name>"
  echo "where the <protein name> is the same as that of it FASTA."
  exit
fi

protein=$1

job_name=${protein}

n_thread=2


start=$(date +%s.%N)

if [ ! -d ${out_dirt}/${job_name} ]
then
  mkdir -p ${out_dirt}/${job_name}
fi

fasta=${seq_dirt}/${protein}.fasta
fasta_wt=${out_dirt}/${job_name}/${protein}_WT.fasta

# date +"%T-%m-%d-%y"
printf "## Leri Analytics is working on protein %s \n" "${protein}"

# Pre-process
printf "## L1. Obtaining FASTA of %s ...\n" "${protein}"

n=`cat ${fasta} | wc | awk '{print $1}'`
echo "`head -1 ${fasta}`" > ${fasta_wt}
for i in `seq 2 ${n}`
do
  cat ${fasta} | head -${i} | tail -1 | while read line; do printf "%s" "$line"; done >> ${fasta_wt}
done
printf "##     Protein name:   %s\n" "${protein}"
printf "##     Residue number: %s\n" "`tail -1 ${fasta_wt} | wc -c`"
# echo "## `tail -1 ${fasta_wt}`"

printf "## L2. Searhing protein (%s) against UniRef%s database ...\n" "${protein}" "${data_idx}"
flag_jackhmmer=0
if [ ! -f ${out_dirt}/${job_name}/${protein}.sto ]; then
  flag_jackhmmer=1
elif [[ -f ${out_dirt}/${job_name}/${protein}.sto  &&  `ls -s ${out_dirt}/${job_name}/${protein}.sto | awk '{print $1}'` -eq 0 ]]; then
  flag_jackhmmer=1
fi
if [ ${flag_jackhmmer} -eq 1 ]; then
  start=`date +%s`
  $jackhmmer --notextw \
  --cpu ${n_thread} \
   -A ${out_dirt}/${job_name}/${protein}.sto \
  --tblout ${out_dirt}/${job_name}/${protein}_tbl.out \
  --domtblout ${out_dirt}/${job_name}/${protein}_domtbl.out \
   -E 0.01 \
  --popen 0.25 \
  --pextend 0.4 \
    ${fasta_wt} \
    ${database} \
  >/dev/null
  #--mxfile ${lib_dirt}/common/BLOSUM62.mat \
  # -T 0.4 \ bit scorce
  end=`date +%s`
  run_time=$((end-start))
  printf "##     Running time: %f" ${run_time}
fi
printf "## L3. Converting from the file (*.sto) of %s generated by jackhmmer to *.a2m ...\n" "${protein}"
${leri} sequence_converter \
-jobname ${job_name} \
-msa ${out_dirt}/${job_name}/${protein}.sto \
-threads ${n_thread} \
-output ${out_dirt}/


printf "## L4. Trimming the obtained MSA of %s ...\n" "${protein}"
${leri} sequence_trim \
-jobname ${job_name} \
-msa ${out_dirt}/${job_name}/${job_name}_msa.a2m \
-gap_frac 0.15 \
-threads ${n_thread} \
-output ${out_dirt}/

printf "## L4. Compute statistics on the aligned sequences of protein %s ...\n" "${protein}"
${leri} sequence_stats \
-jobname ${job_name} \
-msa ${out_dirt}/${job_name}/${job_name}_msa_trimmed.aln \
-threads ${n_thread} \
-max_iter 1000 \
-output ${out_dirt}/

printf "## L5. Compute coupling on the aligned sequences of protein %s ...\n" "${protein}"
${leri} sequence_coupling \
-jobname ${job_name} \
-msa ${out_dirt}/${job_name}/${job_name}_msa.a2m \
-threads ${n_thread} \
-max_iter 10 \
-output ${out_dirt}/

printf "## L6. Point_mutation for protein %s\n" "${protein}"
${leri} point_mutation \
-jobname ${job_name} \
-threads ${n_thread} \
-fastx ${fasta_wt} \
-mat ${out_dirt}/${job_name}/${job_name}_sequence_potential.csv \
-output ${out_dirt}/

printf "## L7. Design sequence for protein %s\n" "${protein}"
${leri} sequence_design \
-jobname ${job_name} \
-threads ${n_thread} \
-fastx ${fasta_wt} \
-mat ${out_dirt}/${job_name}/${job_name}_sequence_potential.csv \
-max_iter 100000 \
-output ${out_dirt}/

printf "## L8. Compute sequence energy for protein %s\n" "${protein}"
${leri} sequence_energy \
-jobname ${job_name} \
-threads ${n_thread} \
-msa ${out_dirt}/${job_name}/${job_name}_msa_trimmed.aln \
-mat ${out_dirt}/${job_name}/${job_name}_sequence_potential.csv \
-output ${out_dirt}/

end=$(date +%s.%N)    
runtime=$(python -c "print(${end} - ${start})")

printf "## L9. Completed in %f\n\n" "${runtime}"
#date +"%T-%m-%d-%y"

```
