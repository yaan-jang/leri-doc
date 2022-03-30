import os, argparse

#########################################################################
psiblast = '/usr/bin/psiblast'
#psiblast = 'ncbi-blast-2.11.0+/bin/psiblast
jackhmmer = '/usr/local/bin/jackhmmer'
mafft = '/usr/local/bin/mafft'
hhblits = '/usr/local/bin/hhblits'
leri = '~/amo/leri-build/tool/leri'  # local version
#########################################################################
dirt_exdrv = '/database/' #  need to change

db_psiblast = dirt_exdrv + 'nr20210808/nr'
# Hhblits can use either UniClust30 or BFD
# BFD (~1.8T): 
# https://storage.googleapis.com/alphafold-databases/casp14_versions/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt.tar.gz
db_uniclust30 = dirt_exdrv + 'uniclust/UniRef30_2020_06'
db_bfd = dirt_exdrv + 'bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt'

# jackhmmer can use either UniRef50, UniRef90, UniRef100, metaclust_nr, or metaclust_50_cluster
db_uniref90 = dirt_exdrv + 'uniref90.fasta'
db_metaclust50 = dirt_exdrv + 'metaclust_50_cluster.fasta'
db_mgnify = dirt_exdrv + 'mgy_clusters.fa'

n_threads = 2
#########################################################################
# Usage:
# python generate_msa.py -s FASTA.fasta -o OUTPUT_DIR
#########################################################################

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--fasta',  type=str, default='')
parser.add_argument('-o', '--output', type=str, default='')
args = parser.parse_args()


def func_mkdir(dirt):
    if not os.path.exists(dirt):
        os.makedirs(dirt)

def get_dirt(target):
    # dirt = os.getcwd()
    dirt = args.output
    dirt_target = dirt + '/L' + target
    dirt_share  = dirt_target + '/share' 
    dirt_tmp    = dirt_target + '/tmp'
    func_mkdir(dirt)
    func_mkdir(dirt_target)
    func_mkdir(dirt_share)
    func_mkdir(dirt_tmp)
    return dirt, dirt_share, dirt_tmp

def str_write(fname, sstr, mod = 'w'):
    with open(fname, mod) as fid:
        if len(sstr) > 0:

            if type(sstr) == list:
                for i in range(len(sstr)):
                   fid.write(sstr[i].strip()+'\n')
            else:
                fid.write(sstr.strip()+'\n')
    fid.close()

def str_write_all(fname, sstr, mod = 'w'):
    fid = open(fname, mod)
    fid.writelines(sstr)
    fid.close()

def read_fasta(target):
    with open(target, 'r') as fid:
        lines = fid.readlines()
        lines = [i for i in lines if len(i.strip()) > 0]
    return lines

def func_leri(opt, target, aln):
    str_info = '-- '
    dirt, dirt_share, dirt_tmp = get_dirt(target)
    raln = ''
    str_cmd  = ''
    if (opt == 'convertor'): # used for jackhmmer
        str_info += 'Converting sequences using LERI ...' 
        str_cmd += leri + ' sequence_converter' + ' '
        str_cmd += '-jobname ' + target + ' '
        str_cmd += '-type 1' + ' '
        str_cmd += '-msa ' + aln + ' '
        str_cmd += '-threads ' + str(n_threads) + ' '
        str_cmd += '-output ' + dirt_tmp + '/' + ' '
        str_cmd += '> /dev/null'
    if (opt == 'trim'):
        str_info += 'Trimming sequences using LERI ...' 
        str_cmd += ''
        str_cmd += leri + ' sequence_trim' + ' '
        str_cmd += '-jobname ' + target + ' '
        str_cmd += '-gap_frac 1.0' + ' '
        str_cmd += '-site_gap_frac 1.0' + ' '
        str_cmd += '-msa ' + aln + ' '
        str_cmd += '-threads ' + str(n_threads) + ' '
        str_cmd += '-output ' + dirt_tmp + '/'
        str_cmd += '> /dev/null'
        raln = dirt_tmp + '/' + target + '/' + target + '_msa_trimmed.a3m'
    str_cmd += '\n'
    # print(raln)
    print(str_info)
    os.system(str_cmd)
    return raln

def func_mafft(target, aln):
    dirt, dirt_share, dirt_tmp = get_dirt(target)
    raln = dirt_tmp + '/' + target + '_PSIBLAST_MAFFT.a3m'
    if not os.path.exists(raln) or os.path.getsize(raln) == 0:
        print('-- Make alignment using MAFFT ...')
        str_cmd  = ''
        str_cmd += mafft + ' --quiet' + ' '
        str_cmd += '--thread ' + str(n_threads) + ' '
        str_cmd += aln + ' ' 
        str_cmd += '> ' + raln
        str_cmd += '\n'
        os.system(str_cmd)
    return raln

def func_phsiblast(target, database, seq, run = False):
    dirt, dirt_share, dirt_tmp = get_dirt(target)
    # fname = dirt_tmp + '/' + target + '_psiblast'
    fname = target + '_PSIBLAST_' + (database.split('/')[-1]).upper()
    if run:
        print('-- Psi-BLAST on ' + target + ' using ' + (database.split('/')[-1]).upper())
        str_cmd  = ''
        str_cmd += psiblast + ' '
        str_cmd += '-db ' + database + ' '
        str_cmd += '-num_iterations 3' + ' '
        str_cmd += '-num_threads ' + str(n_threads) + ' '
        str_cmd += '-out_ascii_pssm ' + dirt_share + '/' + target + '.pssm' + ' '
        str_cmd += '-out ' + dirt_tmp + '/' + fname+'.msa' + ' '
        str_cmd += '-outfmt \'6 sseqid sseq\'' + ' '
        str_cmd += '-query ' + dirt_share + '/' + target + '.fasta' + ' '
        str_cmd += '> /dev/null'
        str_cmd += '\n'
        os.system(str_cmd)
   
    if not os.path.exists(dirt_share+'/'+fname+'.a3m') or os.path.getsize(dirt_share+'/'+fname+'.a3m') == 0:
        # reformat
        str_write(dirt_tmp + '/' + fname + '.a3m', list(), 'w+')
        seq = read_fasta(dirt_share + '/' + target + '.fasta')
        str_write(dirt_tmp + '/' + fname + '.a3m', seq, 'a+') # write query
        with open(dirt_tmp + '/' + fname + '.msa', 'r') as fid:
            lines = fid.readlines()
            for line in lines:
                sline = line[:-1].split('	') # here is a tab
                if sline[0] and "Search" not in sline[0]:
                    sline[0] = '>' + sline[0]
                    str_write(dirt_tmp + '/' + fname + '.a3m', sline, 'a+')
        aln = func_mafft(target, dirt_tmp + '/' + fname + '.a3m')
        aln = func_leri('trim', target, aln)
        str_write(dirt_share+'/'+fname + '.a3m', list(), 'w+')
        with open(aln, 'r') as fid:
            lines = fid.readlines()
            for line in lines:
                str_write(dirt_share+'/'+fname + '.a3m', line, 'a+')
    return dirt_share+'/'+fname+'.a3m'

def func_hhblits(target, database, seq, run = False):
    dirt, dirt_share, dirt_tmp = get_dirt(target)
    fname = target + '_HHBLITS_' + (database.split('/')[-1]).upper()
    if run:
        print('-- HHblits on ' + target + ' using ' + (database.split('/')[-1]).upper())
        str_cmd  = ''
        str_cmd += hhblits + ' '
        str_cmd += '-v 0' + ' '
        str_cmd += '-d ' + database + ' '
        str_cmd += '-cpu ' + str(n_threads) + ' '
        str_cmd += '-n 5' + ' '
        str_cmd += '-E 0.001' + ' '
        str_cmd += '-o ' + dirt_tmp + '/' + fname + '.hhr' + ' '
        str_cmd += '-opsi ' + dirt_tmp + '/' + fname + '.msa' + ' '
        str_cmd += '-i ' + dirt_share + '/' + target + '.fasta' + ' '
        str_cmd += '> /dev/null'
        str_cmd += '\n'
        os.system(str_cmd)

    if not os.path.exists(dirt_share+'/'+fname+'.a3m') or os.path.getsize(dirt_share + '/' + fname+'.a3m') == 0:
        # reformat
        str_write(dirt_tmp + '/' + fname + '.a3m', list(), 'w+')
        with open(dirt_tmp + '/' + fname + '.msa', 'r') as fid:
            lines = fid.readlines()
            for line in lines:
                sline = line.strip().split(' ')
                sline = list(filter(None, sline))
                sline[0] = '>' + sline[0]
                str_write(dirt_tmp + '/' + fname + '.a3m', sline, 'a+')
        fid.close()
        aln = dirt_tmp + '/' + fname + '.a3m'
        aln = func_leri('trim', target, aln)
        with open(aln, 'r') as fid:
            lines = fid.readlines()
            str_write_all(dirt_share+'/'+fname+'.a3m', lines)
        fid.close()
    return dirt_share+'/'+fname+'.a3m'

def func_jackhmmer(target, database, seq, run = False):
    dirt, dirt_share, dirt_tmp = get_dirt(target)
    fname = target + '_HMMER_' + (database.split('/')[-1]).split('.fa')[0].upper()
    if run:
        print('-- HMMER on ' + target + ' using ' + (database.split('/')[-1]).upper())
        str_cmd  = ''
        str_cmd += jackhmmer + ' --notextw' + ' '
        str_cmd += '--cpu ' + str(n_threads) + ' '
        str_cmd += ' -E 0.001' + ' '
        str_cmd += ' -A ' + dirt_tmp + '/' + fname + '.sto' + ' '
        str_cmd += '--tblout ' + dirt_tmp + '/' + fname + '_tbl.out' + ' '
        str_cmd += '--domtblout ' + dirt_tmp + '/' + fname + '_domtbl.out' + ' '
        str_cmd += '--popen 0.25' + ' '
        str_cmd += '--pextend 0.4' + ' '
        str_cmd += dirt_share + '/' + target + '.fasta' + ' '
        str_cmd += database + ' '
        str_cmd += '>/dev/null'
        str_cmd += '\n'
        os.system(str_cmd)

    if not os.path.exists(dirt_share+'/'+fname+'.a3m') or os.path.getsize(dirt_share + '/' + fname+'.a3m') == 0:
        # convert to a3m
        aln = func_leri('convertor', target, dirt_tmp + '/' + fname + '.sto')
        aln = func_leri('trim', target, aln)
        with open(aln, 'r') as fid:
            lines = fid.readlines()
            str_write_all(dirt_share+'/'+fname+'.a3m', lines)
        fid.close()
    return dirt_share+'/'+fname+'.a3m'

def func_msa_assembly(target, msa):
    print('-- Concatenating different alignments ...')
    dirt, dirt_share, dirt_tmp = get_dirt(target)
    fname = dirt_share + '/' + target + '.a3m'
    str_write(fname, list(), 'w+')
    for aln in msa:
        with open(aln, 'r') as fid:
            lines = fid.readlines()
            for line in lines:
                str_write(fname, line, 'a+')
    print('-- Completed!')

def main(target):
    seq = read_fasta(target)
    target = (target.split('/')[-1]).split('.fasta')[0]
    get_dirt(target)
    print('-- Generating an MSA of ' + target + ' from genetic databases ...')
    # print(seq[0][:-1])
    # print(seq[1][:-1])
    dirt, dirt_share, dirt_tmp = get_dirt(target)
    str_write(dirt_share + '/' + target + '.fasta', seq)
    str_write(dirt_share + '/' + target + '.a3m', list())

    msa = list()
    # PSI-BLAST database is generally worse
    # msa.append(func_phsiblast(target, db_psiblast, seq, True))
    # for database in [db_uniclust30]:
    for database in [db_uniclust30, db_bfd]:
        msa.append(func_hhblits(target, database, seq, True))
    for database in [db_uniref90, db_metaclust50, db_mgnify]:
        msa.append(func_jackhmmer(target, database, seq, True))
    func_msa_assembly(target, msa)

if __name__ == '__main__':
    seq = args.fasta
    main(seq)
