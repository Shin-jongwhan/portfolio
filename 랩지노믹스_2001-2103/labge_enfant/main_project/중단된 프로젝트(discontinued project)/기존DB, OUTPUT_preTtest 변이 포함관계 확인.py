def OUT_preTtest_parsing() :
    # delete same segment test
    # Win_logRatio	Group	SegInterval	segSize	seg_logRatio	Existenceof_DB	Var_type	Sample
    # 0.587614276896053	TEST	chr4:190225001-190925000	700000	0.4278	TP	dup	2018122715697-EF3-LT
    fOutput = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\OUT_preTtest_all_201008.txt", 'r')
    fResult = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\OUT_preTtest_all_201008_step1_del_same_CNV.txt", 'w')
    lsResult = []
    lsHeader = fOutput.readline().strip().split("\t")
    fResult.write("\t".join(lsHeader) + "\n")
    print(lsHeader)
    for i in fOutput :
        i = i.strip().split("\t")
        #print(i)
        if lsResult == [] :
            lsResult.append(i)
            lsResult[-1].append(1)
            fResult.write("\t".join(lsResult[-1][:-1]) + "\n")
            #print(lsResult[-1])
        if i[2] == lsResult[-1][2] and i[4] == lsResult[-1][4] and i[6] == lsResult[-1][6] and i[7] == lsResult[-1][7] :
            lsResult[-1][-1] += 1
            continue
        else : 
            lsResult.append(i)
            lsResult[-1].append(1)
            fResult.write("\t".join(lsResult[-1][:-1]) + "\n")
            #print(lsResult[-1])

    nSum = 0
    for i in range(0, len(lsResult)) :
        nSum += lsResult[i][-1]

    print(nSum)     # 688041 : correct


    fOutput.close()
    fResult.close()


def FP_data_check() :
    fPreTtest = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\OUT_3\\OUT_preTtest_3.txt", 'r')
    fDB = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\EnfantGuard_manualcheck_AllTP_DB_200916.txt", 'r')
    fPreTtest_adjust = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\OUT_3\\OUT_preTtest_3_adjust.txt", 'w')
    fPreTtest_adjust_list = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\OUT_3\\OUT_preTtest_3_adjust_list.txt", 'w')

    lsPreTtest_result = []
    lsDB = []

    lsPreTtest_header = fPreTtest.readline().strip().split("\t")
    lsDB_header = fDB.readline().strip().split("\t")

    fPreTtest_adjust_list.write("\t".join(lsPreTtest_header) + "\tDB_sample\n")
    fPreTtest_adjust.write("\t".join(lsPreTtest_header) + "\n")

    for i in fDB :
        lsDB.append(i.strip().split("\t"))

    nCount = 0
    lsSame_var = ["1","1","1","1","1","1","1","1"]      # initialization
    for i in fPreTtest :
        nCount += 1
        if nCount % 10000 == 0  : 
            print(nCount)
        i = i.strip().split("\t")
        sID_test = i[7].split("-")[0]
        sChr_test = i[2].split(":")[0]
        sStart_test = i[2].split(":")[1].split("-")[0]
        sEnd_test = i[2].split(":")[1].split("-")[1]
        sCopy_state_test = i[6]
        #print(sID_test, sChr_test, sStart_test, sEnd_test)
        if i[5] == "FP" :
            blFP_check = False
            if lsSame_var[7].split("-")[0] == sID_test and lsSame_var[2].split(":")[0] == sChr_test and lsSame_var[2].split(":")[1].split("-")[0] == sStart_test and lsSame_var[2].split(":")[1].split("-")[1] == sEnd_test :
                fPreTtest_adjust.write("\t".join(i[:5]) + "\t" + "\t".join(lsSame_var[5:]) + "\n")
                #print("\t".join(i[:5]) + "\t" + "\t".join(lsSame_var[5:]))
                continue
            for j in range(0, len(lsDB)) :
                sID_DB = lsDB[j][1].split("-")[0]
                sChr_DB = lsDB[j][2]
                sStart_DB = lsDB[j][3]
                sEnd_DB = lsDB[j][4]
                sCopy_state_DB = lsDB[j][7]
                #print(sID_DB, sChr_DB, sStart_DB, sEnd_DB)
                if sID_test == sID_DB and sChr_test == sChr_DB and sStart_test == sStart_DB and sEnd_test == sEnd_DB and sCopy_state_test == sCopy_state_DB  :
                    lsPreTtest_result.append(i)
                    lsPreTtest_result[-1].append(lsDB[j][1])        # modified sample name
                    fPreTtest_adjust_list.write("\t".join(lsPreTtest_result[-1]) + "\n")
                    
                    lsWrite_data = lsPreTtest_result[-1][:-1]
                    lsWrite_data[5] = "TP"
                    lsWrite_data[7] = lsDB[j][1]
                    lsSame_var = lsWrite_data
                    #print(lsWrite_data)
                    #lsPreTtest_result[-1][5] = "TP"
                    #lsPreTtest_result[-1][7] = lsDB[j][1]
                    blFP_check = True
                    #print(lsPreTtest_result[-1])
                    fPreTtest_adjust.write("\t".join(lsWrite_data) + "\n")
                    break
            if blFP_check == False :
                fPreTtest_adjust.write("\t".join(i) + "\n")
                #lsPreTtest_result.append(i)
                #print(lsPreTtest_result[-1])
                lsSame_var = i
        else :
            fPreTtest_adjust.write("\t".join(i) + "\n")
            #lsPreTtest_result.append(i)
            #print(lsPreTtest_result[-1])

    fPreTtest.close()
    fDB.close()
    fPreTtest_adjust.close()
    fPreTtest_adjust_list.close()


def data_check_1() : 
    fPreTtest_adjust = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\OUT_3\\OUT_preTtest_3_adjust.txt", 'r')
    for i in fPreTtest_adjust :
        #print(len(i))
        if len(i) > 108 :
            print(len(i))
    fPreTtest_adjust.close()


def main() :
    #OUT_preTtest_parsing()
    #FP_data_check()
    data_check_1()

main()





