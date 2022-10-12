import time
start_time = time.time()

def measured_time(t) :
    # t = time.time() - start_time
    print( "measured time : {0} m {1} s".format( int(t // 60), round( (t % 60), 2 ) ) )


def separ_contig() :
    sFa_dir = "D:\\NGS_data\\data\\fasta\\Marchantia_polymorpha\\Mpo_mature_miR_shihshun.fasta"
    fFa = open(sFa_dir, 'r')
    lsFa = []
    lsFa = fFa.read().split(">")
    del lsFa[0]
    fFa.close()
    print("Number of contig : ", len(lsFa))
    lsWrite = []
    sWrite_dir = "D:\\NGS_data\\software\\miRPlant_V6\\genome\\Mpo_miR\\"
    for i in range(0, len(lsFa)) :
        lsWrite.append( lsFa[i].split(" ")[0]+ ".fa" )
    #print(len(lsWrite), len(lsFa))     for check
    for i in range(0, len(lsFa)) :
        fWrite = open( (sWrite_dir + lsWrite[i]), 'w')
        fWrite.write(">")
        fWrite.write(lsFa[i])
        fWrite.close()
    print("Separator function is done")


def main() :
    print("Start split contig or chr to other files respectively")
    separ_contig()
    measured_time(time.time() - start_time)

main()
