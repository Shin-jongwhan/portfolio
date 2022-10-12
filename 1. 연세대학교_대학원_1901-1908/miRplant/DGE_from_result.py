# parse miRPlant result file and then analyze differential gene expression.
import time
import math
start_time = time.time()
### miR_ID	score	chr	strand	hairPin_loci	expression(number of mature reads)	mature_loci	sequence
### hairPin 2nd second RNA Structure	mature miR	mature_loop_star_seq	reads_no
### novelMiR_1	0.80	chloroplast	+	44715-44854	62	44827-44844
### ccttctatctacttccaaattttccggtcaaaaagggtatctattaaccataatctaaaaaacgatgaataactcgctattcacccagatactcagtcataatcttgatgtcggagagatggccgagtggttgaaggcgt
### (((((...(((((((((..((((((((...................................................................................)))))))).)))..))))))..)))))...
### ggagagatggccgagtgg	acttccaaattttccggtcaaaaagggtatctattaaccataatctaaaaaacgatgaataactcgctattcacccagatactcagtcataatcttgatgtcggagagatggccgagtgg
### [t1458798] chloroplast+44827-44844|62;[t1530782] chloroplast+44867-44884|1#
#
### what tags are required : [0] miR_ID [5] reads count
def measured_time(t) :
    # t = time.time() - start_time
    print( "measured time : {0} m {1} s".format( int(t // 60), round( (t % 60), 2 ) ) )


def parse_result(sFile_name) :
    print("read file name : ", sFile_name)
    fResult = open(sFile_name, 'r')
    lsResult = []       # extract [0], [5]
    lsResult = fResult.read().split("\n")
    fResult.close()
    del lsResult[0]
    del lsResult[-1]
    for i in range(len(lsResult) - 1, -1, -1) :
        lsResult[i] = lsResult[i].split("\t")
        lsResult[i].append(lsResult[i][0])
        lsResult[i].append(lsResult[i][5])
        del lsResult[i][:-2]
        if "novel" in lsResult[i][0] :
            del lsResult[i]
            continue
        if "*" in lsResult[i][0] :
            del lsResult[i]

    for i in range(0, len(lsResult)) :     # for check
        print(lsResult[i])
        
    lsResult = sorted(lsResult, key = lambda element : element[0])
    return lsResult


def append_miR_name(lsResult) :
    lsMIR_name = []
    for i in range(0, len(lsResult)) :
        lsMIR_name.append(lsResult[i][0])      # [0] = miR_name
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


def compare_gene_ex(lsMIR_name, lsResult) :
    for i in range(0, len(lsMIR_name)) :
        lsMIR_name[i].append("0")
        for k in range(0, len(lsResult)) :
            if lsMIR_name[i][0] == lsResult[k][0] :
                lsMIR_name[i][-1] = lsResult[k][-1]
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
    measured_time(time.time() - start_time)
    lsResult_1 = parse_result("D:\\NGS_data\\data\\miRplant\\TAIR10_ref_Mpo\\company_trim\\0h\\0h.R1.clean.result")
    lsResult_2 = parse_result("D:\\NGS_data\\data\\miRplant\\TAIR10_ref_Mpo\\company_trim\\12h\\12h.R1.clean.result")
    lsResult_3 = parse_result("D:\\NGS_data\\data\\miRplant\\TAIR10_ref_Mpo\\company_trim\\24h\\24h.R1.clean.result")
    lsMIR_name = lsMIR_name + append_miR_name(lsResult_1)
    print("len(lsMIR_name)_1 : ", len(lsMIR_name))        # for check
    lsMIR_name = lsMIR_name + append_miR_name(lsResult_2)
    print("len(lsMIR_name)_2 : ", len(lsMIR_name))        # for check
    lsMIR_name = lsMIR_name + append_miR_name(lsResult_3)
    print("len(lsMIR_name)_3 : ", len(lsMIR_name))        # for check
    lsMIR_name = parse_lsMIR_name(lsMIR_name)
    print("\n", "This analysis will refer these miRNA as reference")
    for i in range(0, len(lsMIR_name)) :
        print(lsMIR_name[i])        # for check
    lsMIR_name = compare_gene_ex(lsMIR_name, lsResult_1)
    print("lsMIR_name[0], [-1]_1 : ", lsMIR_name[0], lsMIR_name[-1])        # for check
    lsMIR_name = compare_gene_ex(lsMIR_name, lsResult_2)
    print("lsMIR_name[0], [-1]_2 : ", lsMIR_name[0], lsMIR_name[-1])        # for check
    lsMIR_name = compare_gene_ex(lsMIR_name, lsResult_3)
    print("lsMIR_name[0], [-1]_3 : ", lsMIR_name[0], lsMIR_name[-1])        # for check
    lsDiffer_ex = RPKM(lsMIR_name, 3)
    print(lsDiffer_ex[0], "\n", lsDiffer_ex[-1])
    lsDiffer_ex = fold_change(lsDiffer_ex, 3)

    fWrite = open("C:\\Users\\Shin\\Desktop\\과제\\정박사님 마찬티아 sRNA_seq\\miRplant_AT_mature_miR_ref_Mpo_drought_company_DGE.txt", 'w')
    sDescription = "miR_name\tcount_0h\tcount_12h\tcount_24h\tRPKM_0h\tRPKM_12h\tRPKM24h\tfold_change_12h\tfold_change_24h"
    fWrite.write(sDescription)
    fWrite.write("\n")
    for i in range(0, len(lsDiffer_ex)) :
        fWrite.write("\t".join(lsDiffer_ex[i]))
        fWrite.write("\n")
    fWrite.close()
main()
