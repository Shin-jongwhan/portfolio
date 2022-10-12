## example
#
#@HD	VN:1.0	SO:unsorted
#@SQ	SN:NC_000913.2	LN:4639675
#@PG	ID:Bowtie	VN:1.1.2	CL:"bowtie --wrapper basic-0 -n 3 -p 6 -S /mnt/share/correct/ebwt/Ecoli_NC_009132_2/1 /mnt/share/correct/fastq/Fur_Fe_1_ChIP.fastq"
#SRR1168121.3	16	NC_000913.2	4561717	255	31M	*	0	0	CAATTCAGCGCCAGACACCATCCTGCTGGCN	FB53222ECFGGGGGGGGGFABFFBAA>>>#	XA:i:2	MD:Z:4G25A0	NM:i:2
#
# [0] id, [1] sam flag, [2] reference seq name
import time
start_time = time.time()

def measured_time(t) :
    print( "measured_time : {0} m {1} s".format( int(t // 60), round( (t % 60), 2 ) ) )

def main() :
    sSam_dir = "D:\\NGS_data\\data\\sam\\PhD_jung_hyunju\\marchantia\\company\\AT_mature_miR_ref_Mpo_24h_trim\\AT_mature_miR_ref_Mpo_24h_trim_company.sam"
    sWrite_dir = ".".join(sSam_dir.split(".")[0:-1]) + "_del_samF_4.sam"
    fSam = open(sSam_dir, "r")
    fWrite = open(sWrite_dir, 'w')
    print(round(time.time() - start_time, 2), "s,", "read file : ", sSam_dir.split("\\")[-1] )
    print(round(time.time() - start_time, 2), "s,", "write file : ", sWrite_dir.split("\\")[-1] )
    lsDel_flag_4 = []

    while True :
        i = fSam.readline()
        if "" == i :
            break
        if "@" in i :
            fWrite.write(i)
            continue
        if i.split("\t")[1] == "4" :
            continue
        if i.split("\t")[1] != "4" :
            #lsDel_flag_4.append(i.split("\t"))
            fWrite.write(i)
            
    measured_time( (time.time() - start_time) )
    
    lsDel_flag_4 = sorted(lsDel_flag_4, key = lambda element : element[2])
    
    #for i in range( 0, len(lsDel_flag_4) ) :
        #fWrite.write("\t".join(lsDel_flag_4[i]))

    fSam.close()
    fWrite.close()

main()
