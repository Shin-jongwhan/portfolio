from operator import itemgetter

def split_decision_call_by_QC() :
    fDecision_call = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\업데이트\\Decision_190102-200501_decision_parsing_201020.txt", 'r')
    fQCfail_list = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\업데이트\\QCfail_sample_list_201020.txt", 'r')
    fQCfail_decision_call = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\업데이트\\QCfail_Decision_190102-200501_decision_parsing_201020.txt", 'w')
    fQCpass_decision_call = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\업데이트\\QCpass_Decision_190102-200501_decision_parsing_201020.txt", 'w')

    lsDecision_call_header = fDecision_call.readline().strip().split("\t")
    lsQCfail_list_header = fQCfail_list.readline().strip().split("\t")

    fQCfail_decision_call.write("\t".join(lsDecision_call_header) + "\n")
    fQCpass_decision_call.write("\t".join(lsDecision_call_header) + "\n")

    print(lsDecision_call_header)
    print(lsQCfail_list_header)

    lsDecision_call = fDecision_call.readlines()
    lsQCfail_list = fQCfail_list.readlines()

    for i in range(0, len(lsDecision_call)) :
        lsDecision_call[i] = lsDecision_call[i].strip().split("\t")

    for i in range(0, len(lsQCfail_list)) :
        lsQCfail_list[i] = lsQCfail_list[i].strip().split("\t")

    print(lsDecision_call[0])
    print(lsQCfail_list[0])

    lsQCpass_decision_call = []
    lsQCfail_decision_call = []

    nSample_count = 0
    for i in range(0, len(lsDecision_call)) :
        for j in range(0, len(lsQCfail_list)) :
            if lsDecision_call[i][1] == lsQCfail_list[j][1] :
                lsQCfail_decision_call.append(lsDecision_call[i])
                #print("\t".join(lsDecision_call[i]))
                nSample_count += 1
                fQCfail_decision_call.write("\t".join(lsDecision_call[i]) + "\n")
                break
            else :
                if j == len(lsQCfail_list) - 1 : 
                    lsQCpass_decision_call.append(lsDecision_call[i])
                    fQCpass_decision_call.write("\t".join(lsDecision_call[i]) + "\n")

    print(nSample_count)

    fDecision_call.close()
    fQCfail_list.close()
    fQCfail_decision_call.close()
    fQCpass_decision_call.close()


def count_sample_func(lsDecision_call, fWrite) :
    fWrite.write("run_id\tsample\n")
    nCount_sample = 0
    lsCount_sample = []
    for i in range(0, len(lsDecision_call)) :
        if lsCount_sample == [] :
            lsCount_sample = lsDecision_call[i]
            fWrite.write(lsDecision_call[i][0] + "\t" + lsDecision_call[i][1] + "\n")
            nCount_sample += 1
        if lsCount_sample[1] == lsDecision_call[i][1] :
            continue
        else :
            lsCount_sample = lsDecision_call[i]
            fWrite.write(lsDecision_call[i][0] + "\t" + lsDecision_call[i][1] + "\n")
            nCount_sample += 1
    print("Number of sample : {0}".format(nCount_sample))
    print("")


def count_sample() :
    fQCfail_decision_call = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\업데이트\\QCfail_Decision_190102-200501_decision_parsing_201020.txt", 'r')
    fQCpass_decision_call = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\업데이트\\QCpass_Decision_190102-200501_decision_parsing_201020.txt", 'r')
    fQCfail_sample_list_from_QCfail = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\업데이트\\QCfail_sample_list_from_decision_call_201020.txt", 'w')
    fQCpass_sample_list_from_QCfail = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\업데이트\\QCpass_sample_list_from_decision_call_201020.txt", 'w')
    
    fQCfail_decision_call.readline()    # del header line
    fQCpass_decision_call.readline()    # del header line
    
    lsQCfail_decision_call = fQCfail_decision_call.readlines()
    lsQCpass_decision_call = fQCpass_decision_call.readlines()
    
    for i in range(0, len(lsQCfail_decision_call)) :
        lsQCfail_decision_call[i] = lsQCfail_decision_call[i].strip().split("\t")

    for i in range(0, len(lsQCpass_decision_call)) :
        lsQCpass_decision_call[i] = lsQCpass_decision_call[i].strip().split("\t")
        
    lsQCfail_decision_call.sort(key = itemgetter(2))
    lsQCpass_decision_call.sort(key = itemgetter(2))

    print("Count QCfail sample")
    count_sample_func(lsQCfail_decision_call, fQCfail_sample_list_from_QCfail)
    print("Count QCpass sample")
    count_sample_func(lsQCpass_decision_call, fQCpass_sample_list_from_QCfail)

    fQCfail_decision_call.close()
    fQCpass_decision_call.close()
    fQCfail_sample_list_from_QCfail.close()
    fQCpass_sample_list_from_QCfail.close()


def split_preTtest_by_QC() :
    # to count QCfail sample from preTtest
    fPreTtest = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\all\\OUT_preTtest_all_201008_step1_del_same_CNV.txt", 'r')
    fQCfail_list = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\업데이트\\QCfail_sample_list_201020.txt", 'r')
    fQCfail_pre = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\all\\OUT_preTtest_all_201008_step1_del_same_CNV_QCfail.txt", 'w')
    fQCpass_pre = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\all\\OUT_preTtest_all_201008_step1_del_same_CNV_QCpass.txt", 'w')

    lsPreTtest_header = fPreTtest.readline().strip().split("\t")
    print(lsPreTtest_header)
    lsQCfail_list_header = fQCfail_list.readline().strip().split("\t")

    fQCfail_pre.write("\t".join(lsPreTtest_header) + "\n")
    fQCpass_pre.write("\t".join(lsPreTtest_header) + "\n")
    
    lsPreTtest = fPreTtest.readlines()
    lsQCfail_list = fQCfail_list.readlines()
    
    for i in range(0, len(lsPreTtest)) :
        lsPreTtest[i] = lsPreTtest[i].strip().split("\t")

    for i in range(0, len(lsQCfail_list)) :
        lsQCfail_list[i] = lsQCfail_list[i].strip().split("\t")

    print(lsPreTtest[0])
    print(lsQCfail_list[0])

    lsQCfail_pre = []
    lsQCpass_pre = []

    for i in range(0, len(lsPreTtest)) :
        #print(lsPreTtest[i][7])
        for j in range(0, len(lsQCfail_list)) :
            if lsPreTtest[i][7] == lsQCfail_list[j][1] :
                lsQCfail_pre.append(lsPreTtest[i])
                print("\t".join(lsPreTtest[i]))
                nSample_count += 1
                fQCfail_pre.write("\t".join(lsPreTtest[i]) + "\n")
                break
            else :
                if j == len(lsQCfail_list) - 1 : 
                    lsQCpass_pre.append(lsPreTtest[i])
                    fQCpass_pre.write("\t".join(lsPreTtest[i]) + "\n")

    fPreTtest.close()
    fQCfail_list.close()
    fQCfail_pre.close()
    fQCpass_pre.close()


def samplelist_check() :
    fTest_samplelist = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\Confirm_sample_list_JH_200831.txt", 'r')
    fDB_samplelist = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\업데이트\\앙팡_업데이트_샘플_201020_190102-200501_결과전송.txt", 'r', encoding = "utf-8")

    lsTest_samplelist = fTest_samplelist.readlines()
    lsDB_samplelist = fDB_samplelist.readlines()

    for i in range(0, len(lsTest_samplelist)) :
        lsTest_samplelist[i] = lsTest_samplelist[i].strip().split("\t")

    for i in range(0, len(lsDB_samplelist)) :
        lsDB_samplelist[i] = lsDB_samplelist[i].strip().split("\t")
    
    for i in range(0, len(lsDB_samplelist)) :
        for j in range(0, len(lsTest_samplelist)) :
            if lsDB_samplelist[i][1] == lsTest_samplelist[j][1] :
                break
            else :
                if j == len(lsTest_samplelist) -1 :
                    print(lsDB_samplelist[i])
                    

    for i in range(0, len(lsTest_samplelist)) :
        for j in range(0, len(lsDB_samplelist)) :
            if lsTest_samplelist[i][1] == lsDB_samplelist[j][1] :
                break
            else :
                if j == len(lsDB_samplelist) - 1 :
                    print(lsTest_samplelist[i])


def count_sample_preTtest() :
    fPreTtest_all = open("C:\\Users\\user\\Desktop\\업무\과제\\앙팡가드\\1.개발자료\\최종output_201008\\all\\OUT_preTtest_all_201008_step1_del_same_CNV.txt", 'r')
    lsPreTtest_all_header = fPreTtest_all.readline().strip().split("\t")
    lsPreTtest_all = fPreTtest_all.readlines()

    for i in range(0, len(lsPreTtest_all)) :
        lsPreTtest_all[i] = lsPreTtest_all[i].strip().split("\t")

    lsPreTtest_all.sort(key = itemgetter(7))        # [7] = sample
    #print(lsPreTtest_all[0])
    #print(lsPreTtest_all[-1])

    nCount_sample = 0
    lsSample_tmp = []
    for i in range(0, len(lsPreTtest_all)) :
        #print(lsPreTtest_all[i][7])
        if lsSample_tmp == [] :
            lsSample_tmp = lsPreTtest_all[i]
            nCount_sample += 1
            continue
        if lsSample_tmp[7] == lsPreTtest_all[i][7] :
            continue
        else :
            lsSample_tmp = lsPreTtest_all[i]
            nCount_sample += 1

    print("Counted sample in preTtest.txt : {0}".format(nCount_sample))

    fPreTtest_all.close()
    


def main() :
    #samplelist_check()
    count_sample_preTtest()

    
main()
