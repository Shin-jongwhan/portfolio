# fastq file reading test
def main() :
    sFastq_dir = "D:\\NGS_data\\PhD_jung_hyunju\\2019HC039_small_20190405010442\\24h.R1.fq"
    fFastq = open(sFastq_dir, 'r')
    lsFastq = []
    
    for i in range(0, 1000) :
        lsFastq.append( fFastq.readline() )
        
    fFastq.close()
    fWrite = open( (".".join(sFastq_dir.split(".")[0:-1]) + "_read_test.fq"), 'w')
    for i in range(1, 1000, 4) :
        fWrite.write(lsFastq[i])
    fWrite.close()

main()
