# If you wanna analyze data, please change the file_dir 1. RPKM_fasta, 2. samples, 3. fWrite
import time
import math
start_time = time.time()
# NS500459:508:HMMT7BGX9:4:11503:3035:16820	16	ath-miR156d-3p	1	8	15M	*	0	0
# GCTGACTCTCTTTTT	EEEEEAAEEEAAAAA	AS:i:-5	XN:i:0	XM:i:1	XO:i:0	XG:i:0	NM:i:1	MD:Z:3C11	YT:Z:UU		3
# [1] sam_flag [2] gene_name [9] seq [-1] counted number of miR_name
def measured_time(t) :
    # t = time.time() - start_time
    print( "measured time : {0} m {1} s".format( int(t // 60), round( (t % 60), 2 ) ) )
    

def make_lsSam(file_name) :
    sFile_dir = "D:\\NGS_data\\data\\sam\\" + file_name
    print("read file name : ", sFile_dir)
    fCounted_sam = open(sFile_dir, 'r')
    lsCounted_sam = fCounted_sam.read().split("\n")
    fCounted_sam.close()
    del lsCounted_sam[-1]

    nAlign_sec_start = 0        # initialization for alignment start section site
    for i in range(0, len(lsCounted_sam)) :
        if "@" in lsCounted_sam[i] :
            if "@" not in lsCounted_sam[i + 1] :
                nAlign_sec_start = i + 1
                break
    #measured_time(time.time() - start_time)
    #print("check whether nAlign_section_start number is correct or not")
    #print( "lsSam[nAlign_sec_start -1] : \n{0}\nlsSam[nAlign_sec_start] : \n{1}".format( lsCounted_sam[nAlign_sec_start - 1], lsCounted_sam[nAlign_sec_start] ) )
    #print()
    lsCounted_sam = lsCounted_sam[nAlign_sec_start : ]
    lsCounted_sam = sorted(lsCounted_sam, key = lambda element : element[2])        # for sure, sort by gene name [2]
    for i in range(0, len(lsCounted_sam)) :
        lsCounted_sam[i] = lsCounted_sam[i].split("\t")
    measured_time(time.time() - start_time)
    print("make_lsSam function is done")
    print()
    return lsCounted_sam


def append_miR_name(lsSam) :
    lsMIR_name = []
    for i in range(0, len(lsSam)) :
        lsMIR_name.append(lsSam[i][2])      # [2] = miR_name
    #print(lsMIR_name[0], lsMIR_name[-1])       # for check
    return lsMIR_name


def parse_lsMIR_name(lsMIR_name) :
    # make list of miRNA name for miR_reference to analyze differential gene expression
    lsMIR_name = sorted(lsMIR_name)
    for i in range(len(lsMIR_name) - 1, 0, -1) :
        if lsMIR_name[i] == lsMIR_name[i - 1] :
            del lsMIR_name[i]       # delete if there is name name
        else : continue
    for i in range(0, len(lsMIR_name)) :
        lsMIR_name[i] = [ lsMIR_name[i] ]
    return lsMIR_name


def compare_gene_ex(lsMIR_name, lsSam) :
    for i in range(0, len(lsMIR_name)) :
        lsMIR_name[i].append("0")
        for k in range(0, len(lsSam)) :
            if lsMIR_name[i][0] == lsSam[k][2] :
                lsMIR_name[i][-1] = lsSam[k][-1]
                break
    return lsMIR_name


def RPKM(lsDiffer_ex, n) :
    # this function is limited to transcriptome and miRNA gene.fasta etc... not genomic reference
    # RPKM = (reads count mapped to a gene * 10^3 * 10^6) / (total reads * gene length in bp)
    #fRefer_data : for extracting gene length
    fRefer_fasta = open("D:\\NGS_data\\data\\fasta\\arabidopsis_thaliana\\miRNA\\arabidopsis_thaliana_mature_miRNA.pl_replace_U.fasta", 'r')
    lsRe_fa = []
    while True :
        i = fRefer_fasta.readline()
        if ">" in i :
            if " " in i :
                lsRe_fa.append( [ i[1 : i.find(" ")] ] )
                lsRe_fa[-1].append(fRefer_fasta.readline()[:-1])
            else :
                lsRe_fa.append( [ i[1:-1] ] )
                lsRe_fa[-1].append(fRefer_fasta.readline()[:-1])
        if "" == i :
            break
    for i in range(0, len(lsRe_fa)) :
        lsRe_fa[i].append(len(lsRe_fa[i][-1]))      # int, num of nt
        #print(lsRe_fa[i])      # for check
    fRefer_fasta.close()
    
    lsTotal_reads = []
    for k in range(1, n + 1) :
        for i in range(0, len(lsDiffer_ex)) :
            if i == 0 :
                lsTotal_reads.append(int(lsDiffer_ex[i][k]))
            else :
                lsTotal_reads[-1] += int(lsDiffer_ex[i][k])
    for i in range(0, len(lsTotal_reads)) :
        print("number {0} data Total reads : {1}".format( str(i + 1), lsTotal_reads[i] ) )

    # FPKM = count reads mapped to a gene * 10^9 / (miR_seq len(nt) len(lsRe_fa[i][1]) * total reads[k])
    # lsTotal_reads, lsRe_fa[i][-1] = num of nt of the gene
    # lsDiffer_ex[0] : miR_name, [1] : sample 1 counted num, [2] 2, [3]
    # lsRe_fa[0] : miR_name, [1] seq, [2] len(seq)
    for k in range(1, n + 1) :
        for i in range(0, len(lsDiffer_ex)) :
            for j in range(0, len(lsRe_fa)) :
                if lsRe_fa[j][0] == lsDiffer_ex[i][0] :
                    #print(k, lsRe_fa[j][0], lsDiffer_ex[i][0], lsDiffer_ex[i][k], lsRe_fa[j][-1], lsTotal_reads[k-1])      # for check
                    ###lsDiffer_ex[i].append( str(round( ( ( int(lsDiffer_ex[i][k]) * 10**9 ) / ( lsRe_fa[j][-1] * lsTotal_reads[k-1]) ) + 0.0000000001)) )     # RPKM
                    lsDiffer_ex[i].append( str(round( ( ( int(lsDiffer_ex[i][k]) * 10**6 ) / ( lsRe_fa[j][-1] * lsTotal_reads[k-1]) ) + 0.0000000001)) )     # RPM
    #for i in range(0, len(lsDiffer_ex)) :
    #    print(lsDiffer_ex[i])       # for check
    return lsDiffer_ex


def fold_change(lsDiffer_ex, n) :
    # [n + 1] = control RPKM or RPM
    nAppend = -1
    for k in range(n + 2, n + 4) :
        nAppend += 1
        for i in range(0, len(lsDiffer_ex)) :
            if lsDiffer_ex[i][-n - nAppend] != "0" and lsDiffer_ex[i][k] != "0" :
                lsDiffer_ex[i].append( str( round( math.log2( float( lsDiffer_ex[i][k] ) / float( lsDiffer_ex[i][-n - nAppend] ) ), 2 ) ) )
            else :
                lsDiffer_ex[i].append("-")
    return lsDiffer_ex
            

def main() :
    lsMIR_name = []
    lsSam_1 = make_lsSam("PhD_jung_hyunju\\marchantia\\my_trimming_data\\AT_mature_miR_ref_Mpo_0h_drought_trim\\AT_mature_miR_ref_Mpo_0h_drought_trim_del_samFlag_4_miR_count.sam")
    lsSam_2 = make_lsSam("PhD_jung_hyunju\\marchantia\\my_trimming_data\\AT_mature_miR_ref_Mpo_12h_drought_trim\\AT_mature_miR_ref_Mpo_12h_drought_trim_del_samFlag_4_miR_count.sam")
    lsSam_3 = make_lsSam("PhD_jung_hyunju\\marchantia\\my_trimming_data\\AT_mature_miR_ref_Mpo_24h_drought_trim\\AT_mature_miR_ref_Mpo_24h_drought_trim_del_samFlag_4_miR_count.sam")
    lsMIR_name = lsMIR_name + append_miR_name(lsSam_1)
    print("len(lsMIR_name)_1 : ", len(lsMIR_name))        # for check
    lsMIR_name = lsMIR_name + append_miR_name(lsSam_2)
    print("len(lsMIR_name)_2 : ", len(lsMIR_name))        # for check
    lsMIR_name = lsMIR_name + append_miR_name(lsSam_3)
    print("len(lsMIR_name)_3 : ", len(lsMIR_name))        # for check
    lsMIR_name = parse_lsMIR_name(lsMIR_name)
    lsMIR_name = compare_gene_ex(lsMIR_name, lsSam_1)
    print("lsMIR_name[0], [-1]_1 : ", lsMIR_name[0], lsMIR_name[-1])        # for check
    lsMIR_name = compare_gene_ex(lsMIR_name, lsSam_2)
    print("lsMIR_name[0], [-1]_2 : ", lsMIR_name[0], lsMIR_name[-1])        # for check
    lsMIR_name = compare_gene_ex(lsMIR_name, lsSam_3)
    print("lsMIR_name[0], [-1]_3 : ", lsMIR_name[0], lsMIR_name[-1])        # for check
    lsDiffer_ex = RPKM(lsMIR_name, 3)
    lsDiffer_ex = fold_change(lsDiffer_ex, 3)

    fWrite = open("C:\\Users\\Shin\\Desktop\\과제\\정박사님 마찬티아 sRNA_seq\\AT_mature_miR_ref_Mpo_drought_JH_DGE.txt", 'w')
    sDescription = "miR_name\tcount_0h\tcount_12h\tcount_24h\tRPKM_0h\tRPKM_12h\tRPKM24h\tfold_change_12h\tfold_change_24h"
    fWrite.write(sDescription)
    fWrite.write("\n")
    for i in range(0, len(lsDiffer_ex)) :
        fWrite.write("\t".join(lsDiffer_ex[i]))
        fWrite.write("\n")
    fWrite.close()
main()
