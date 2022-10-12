import time
start_time = time.time()

def measured_time(t) :
    # t = time.time() - start_time
    print( "measured_time : {0} m {1} s".format( int(t // 60), round( (t % 60), 2 ) ) )


def main(sFastq_name) :
    # Ph.D_jung_hyunju marchantia sRNA seq part of P5 primer started at 5' location : TGGAATTC
    # The 'P5 primer' seq is all identical in 0h, 12h, 24h fq file
    sFastq_dir = "D:\\NGS_data\\PhD_jung_hyunju\\2019HC039_small_20190405010442\\" + sFastq_name
    sWrite_dir = ".".join(sFastq_dir.split(".")[0:-1]) + "_trim_primer.fq"
    print(round(time.time() - start_time, 2), "s,", "read file : ", sFastq_dir.split("\\")[-1] )
    print(round(time.time() - start_time, 2), "s,", "write file : ", sWrite_dir.split("\\")[-1] )
    fFastq = open(sFastq_dir, "r")
    fWrite = open(sWrite_dir, 'w')
    nTotal_reads = 0
    nExcept_reads = 0
    nBelow_15_reads = 0

    while True :
        i = fFastq.readline()
        if "@" in i :
            k = fFastq.readline()
            nTotal_reads += 1
            if "TGGAATTC" in k :
                if len( k[ 0 : k.find("TGGAATTC") ] ) >= 15 :
                    fWrite.write(i)     # id
                    fWrite.write(k[ 0 : k.find("TGGAATTC") ])     # seq
                    fWrite.write("\n")
                    fWrite.write(fFastq.readline())      # +
                    fWrite.write( fFastq.readline()[0 : k.find("TGGAATTC") ] )       # quality
                    fWrite.write("\n")
                    continue
                else :
                    fFastq.readline()
                    fFastq.readline()
                    nBelow_15_reads += 1
            else :
                fFastq.readline()
                fFastq.readline()
                nExcept_reads += 1
        if "" == i :
            break
    # while loop end
    nExcept_ratio = round( ( (nExcept_reads + nBelow_15_reads) / nTotal_reads ), 2)
    nWrote_ratio = 1 - nExcept_ratio
    nWrote_reads = nTotal_reads - (nExcept_reads + nBelow_15_reads)
    measured_time(time.time() - start_time)
    print("Total reads : ", nTotal_reads)
    print("Number of excepted reads and 15nt below reads : {0}, {1} ".format(nExcept_reads, nBelow_15_reads))
    print("Number of wrote reads : ", nWrote_reads)
    print("Excepted and wrote Ratio : {0}, {1}".format(nExcept_ratio, nWrote_ratio))
    print()
    

    fFastq.close()
    fWrite.close()
    
main("12h.R1.fq")
main("24h.R1.fq")
