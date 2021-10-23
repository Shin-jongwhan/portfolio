import time
start_time = time.time()

def measured_time(t) :
    # t = time.time() - start_time
    print( "measured time : {0} m {1} s".format( int(t // 60), round( (t % 60), 2 ) ) )


def compare_seq() :
    #sClean_fq : it has sequence only
    sPuri_fa_dir = "D:\\NGS_data\\raw_data\\PhD_jung_hyunju\\miRDeep_analysis_result\\analysisData.190530\\0h\\0h.R1.clean.purify.fa"
    sClean_fq_dir = "D:\\NGS_data\\raw_data\\PhD_jung_hyunju\\0h.R1.clean.fq\\0h.R1.clean_extract_seq.txt"
    fPuri = open(sPuri_fa_dir, 'r')
    fClean = open(sClean_fq_dir, 'r')
    lsPuri = []
    lsClean = []
    while True :
        # to extract sequence only
        i = fPuri.readline()
        if i == "" :
            break
        if ">" in i :
            k = fPuri.readline()
            k = k.replace("\n", "")
            lsPuri.append(k)
    
    lsClean = fClean.read().split("\n")
    del lsClean[-1]
    lsClean = sorted(lsClean)
    print(lsClean[0], lsClean[-1])
    fPuri.close()
    fClean.close()

    nCount_in = 0
    nCheck = 0
    nStart = 0
    for i in range(0, len(lsPuri)) :
        nCheck += 1
        if nCheck % 10000 == 0 :
            print("{0} list is counted".format(str(nCheck)))
        for k in range(nStart, len(lsClean)) :
            if lsPuri[i] in lsClean[k] :
                nCount_in += 1
                nStart = k
                break
    print("Counted Puri.fa sequence (if the sequence is in the clean.fq, increase + 1) : ", nCount_in)


def extract_seq_by_length() :
    #sClean_fq : it has sequence only
    sClean_fq_dir = "D:\\NGS_data\\raw_data\\PhD_jung_hyunju\\0h.R1.clean.fq\\0h.R1.clean_extract_seq.txt"
    fClean = open(sClean_fq_dir, 'r')
    lsClean = []
    while True :
        i = fClean.readline()
        if i == "" :
            break
        i = i.replace("\n", "")
        if 18 <= len(i) and 23 >= len(i) :
            lsClean.append(i)

    measured_time(time.time() - start_time)
    lsClean = sorted(lsClean)
    fWrite = open("_".join(sClean_fq_dir.split("_")[:-2]) + "_18to23.txt", 'w')
    for i in range(0, len(lsClean)) :
        fWrite.write(lsClean[i])
        fWrite.write("\n")
    fWrite.close()


extract_seq_by_length()
    
    

