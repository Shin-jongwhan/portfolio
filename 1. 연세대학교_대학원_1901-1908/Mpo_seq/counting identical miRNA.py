# miR_name count = 가장 많은 것 대표로 보이게 만들기 
import time
start_time = time.time()

def count_function(lsSam, index) :
    nCount = 1      #initialization
    lsMIR_list = []     #initialization
    for i in range(0, len(lsSam)) :
        if i < len(lsSam) - 1 :
            if lsSam[i][index] == lsSam[i + 1][index]:
                nCount += 1
                continue
            elif lsSam[i][index] != lsSam[i + 1][index] :
                lsMIR_list.append(lsSam[i])
                lsMIR_list[-1].append( str(nCount) )
                nCount = 1
                continue
        elif i == len(lsSam) - 1 :
            if lsSam[i][index] == lsSam[i - 1][index] :
                lsMIR_list.append(lsSam[i])
                lsMIR_list[-1].append( str(nCount) )
            else :
                nCount = 1
                lsMIR_list.append( lsSam[i] )
                lsMIR_list[-1].append( str(nCount) )
    # for loop end
    return lsMIR_list


def count_seq_function(lsSam, index) :
    nCount = 1      #initialization
    lsMIR_list = []     #initialization
    for i in range(0, len(lsSam)) :
        if i < len(lsSam) - 1 :
            if lsSam[i][2] == lsSam[i + 1][2] : 
                if lsSam[i][index] == lsSam[i + 1][index]:
                    nCount += 1
                elif lsSam[i][index] != lsSam[i + 1][index] :
                    lsMIR_list.append(lsSam[i])
                    lsMIR_list[-1].append( str(nCount) )
                    nCount = 1
                continue
            elif lsSam[i][2] != lsSam[i + 1][2] :
                lsMIR_list.append(lsSam[i])
                lsMIR_list[-1].append( str(nCount) )
                nCount = 1
        elif i == len(lsSam) - 1 :
            if lsSam[i][2] == lsSam[i - 1][2] :
                if lsSam[i][index] == lsSam[i - 1][index] :
                    lsMIR_list.append(lsSam[i])
                    lsMIR_list[-1].append( str(nCount) )
                else :
                    lsMIR_list.append(lsSam[i])
                    lsMIR_list[-1].append( str(nCount) )        # in this case, nCount = 1
            else :
                lsMIR_list.append(lsSam[i])
                lsMIR_list[-1].append( str(nCount) )        #in this case, nCount = 1
    # for loop end
    return lsMIR_list


def del_small_count(lsMIR_list, n) :
    print( (time.time() - start_time), "delete counted identical mapped sequence to the miRNA, the total number is less than {0} times...".format(n))
    print("len(lsMIR_list) before delete less than {0} : ".format(n), len(lsMIR_list))
    nCount = 0      # initialization
    nEnd_index = len(lsMIR_list)      # initialization
    for i in range(len(lsMIR_list) - 1, -1, -1) :
        if i == (len(lsMIR_list) - 1 ) :
            if lsMIR_list[i][2] == lsMIR_list[i - 1][2] :
                nCount += int( lsMIR_list[i][-1] )
            else :
                del lsMIR_list[i]
                nEnd_index = i
        elif i > 0 and i < (len(lsMIR_list) - 1 ) :
            if lsMIR_list[i][2] == lsMIR_list[i - 1][2] :
                nCount += int(lsMIR_list[i][-1])
            elif lsMIR_list[i][2] != lsMIR_list[i - 1][2] :
                nCount += int( lsMIR_list[i][-1] )
                if nCount < n :
                    print("i, nEnd_index : ", i, nEnd_index)
                    del lsMIR_list[i:nEnd_index]
                    nEnd_index = i
                    nCount = 0
                else :
                    nEnd_index = i
                    nCount = 0
        elif i == 0 :
            if lsMIR_list[i][2] == lsMIR_list[i + 1][2] :
                nCount += int( lsMIR_list[i][-1] )
                if nCount < n :
                    del lsMIR_list[i:nEnd_index]
            else :
                if int( lsMIR_list[i][-1] ) < n :
                    del lsMIR_list[i]
    #for loop end


def start_align_section(lsSam) :
    nStart_align_sec = 0        #start position of alignment_section
    for i in range(0, len(lsSam)) :
        if "@" in lsSam[i][0] :
            if "@" not in lsSam[i + 1][0] :
                nStart_align_sec = i + 1
                break
    return nStart_align_sec
    


def miRNA_count() :
    ## this function don't consider the "N" nuc
    ## thus, if you consider the "N" nuc, sort by seq and count
    ## and then sort by gene name
    # calculate how many each miRNA counted in sam_file
    # [1] sam flag, [2] gene name (ex) ath-imR156a-3p)
    # [5] num of nt, [9] sequence, [10] quality
    sSam_dir = "D:\\NGS_data\\data\\sam\\PhD_jung_hyunju\\marchantia\\company\\AT_mature_miR_ref_Mpo_24h_trim\\AT_mature_miR_ref_Mpo_24h_trim_company_del_samF_4.sam"
    print( (time.time() - start_time), "Read file : ", sSam_dir)
    fSam = open(sSam_dir, 'r')
    lsSam = fSam.read().split("\n")
    fSam.close()
    del lsSam[-1]
    for i in range(0, len(lsSam)) :
        lsSam[i] = lsSam[i].split("\t")

    nStart_align_sec = start_align_section(lsSam)
    
    lsSam[nStart_align_sec : ] = sorted(lsSam[nStart_align_sec : ], key = lambda element:element[2])
    lsMIR_list = count_function(lsSam[nStart_align_sec : ], 2)
    print("len(lsSam_start_align_section) : ", len(lsSam[nStart_align_sec : ]))
    nTotal_count = 0
    for i in range(0, len(lsMIR_list)) :
        nTotal_count += int(lsMIR_list[i][-1])
    print("Total counted number : ", str(nTotal_count))

    # fill "\t" at absent sentence
    for i in range(0, len(lsMIR_list)) :
        if len(lsMIR_list[i]) == 20 :
            lsMIR_list[i][-2] = lsMIR_list[i][-2] + "\t"
            
    print((time.time() - start_time), "Write file...")
    sCount_miR_dir = ".".join(sSam_dir.split(".")[0:-1]) + "_miR_count.sam"
    fCount_miR_sam = open(sCount_miR_dir, 'w')
    for i in range(0, nStart_align_sec) :
        fCount_miR_sam.write( "\t".join( lsSam[i] ) )
        fCount_miR_sam.write("\n")
    for i in range(0, len(lsMIR_list)) :
        fCount_miR_sam.write( "\t".join( lsMIR_list[i] ) )
        fCount_miR_sam.write("\n")
    fCount_miR_sam.close()
    print("Total measure time : ", (time.time() - start_time))


def iden_seq_count() :
    # 1. append each miRNA into list which have more than 100 identical miRNA mapped reads matching
    # 2. sort by mapping sequence and count the identical sequence
    # 3. sort again by miRNA name 
    sSam_dir = "D:\\NGS_data\\data\\sam\\PhD_jung_hyunju\\marchantia\\my_trimming_data\\AT_mature_miR_ref_Mpo_24h_drought_trim\\AT_mature_miR_ref_Mpo_24h_drought_trim_del_samFlag_4.sam"
    print( (time.time() - start_time), "Read file : ", sSam_dir)
    fSam = open(sSam_dir, 'r')
    lsSam = fSam.read().split("\n")
    fSam.close()
    del lsSam[-1]
    for i in range(0, len(lsSam)) :
        lsSam[i] = lsSam[i].split("\t")
    nStart_align_sec = start_align_section(lsSam)
    lsSam[nStart_align_sec : ] = sorted(lsSam[nStart_align_sec : ], key = lambda element:element[2])      # sort by miRNA name
    lsSam[nStart_align_sec : ] = sorted(lsSam[nStart_align_sec : ], key = lambda element:element[9])      # sort by mapped reads sequence
    print( (time.time() - start_time), "count the identical mapped sequence...")

    lsMIR_list = count_seq_function(lsSam[nStart_align_sec : ], 9)
    
    print( (time.time() - start_time), "count function is done")
    lsMIR_list = sorted(lsMIR_list, key = lambda element:element[2])        #sort by miRNA name
    
    #lsMIR_list = sorted(lsMIR_list, key = lambda element:element[-1], reverse = True)        #sort by counted identical mapped reads
    #print(lsMIR_list[0])
    #print(lsMIR_list[-1])
    #lsMIR_list = sorted(lsMIR_list, key = lambda element:element[2])        #sort by miRNA name
    #print("len(lsMIR_list) after delete less than 100 : ", len(lsMIR_list))
    for i in range(0, len(lsMIR_list)) :
        if len(lsMIR_list[i]) == 20 :
            lsMIR_list[i][-2] = lsMIR_list[i][-2] + "\t"
    print((time.time() - start_time), "Write file...")
    sCount_seq_dir = "\\".join( sSam_dir.split("\\")[:-1] ) + "\\" + sSam_dir.split("\\")[-1][:-4] + "_seq_count.sam"
    fCount_seq_sam = open(sCount_seq_dir, 'w')
    for i in range(0, len(lsMIR_list)) :
        fCount_seq_sam.write( "\t".join( lsMIR_list[i] ) )
        fCount_seq_sam.write("\n")
    fCount_seq_sam.close()
    print("Total measure time : ", (time.time() - start_time))


miRNA_count()
iden_seq_count()
