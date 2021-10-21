import os
import sys, getopt

#for i, str in enumerate(sys.argv) :
#    print("%d : %s" %(i, str))

def getopt() :
    optlist = []
    for i, str in enumerate(sys.argv) :
        optlist.append(str)
    return optlist
    

def test_result(sSample_dir, lsSample) :
    sSample_dir_ori = sSample_dir
    #fResult = open("C:\\Users\\shin\\Desktop\\EnfantGuard_test_report_result.txt", 'w')        # for windows
    fResult = open("/home/shinejh0528/EnfantGuard_test_report_result.txt", 'w')
    lsHeader = []
    lsDescription = []
    boolHeader = True
    for i in range(0, len(lsSample)) :
        if len(lsSample[i]) != 1 : 
                sSample_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/" + lsSample[i][0] + "/"
                lsSample[i] = lsSample[i][1]
        else : 
                lsSample[i] = lsSample[i][0]
        lsDescription_sample = []
        #sSample_result_dir = sSample_dir + i + "\\"     # for windows
        #sSample_info_dir = sSample_dir + i + "\\" + i + "\\"        # for windows
        sSample_result_dir = sSample_dir + lsSample[i] + "/"     # for linux
        sSample_info_dir = sSample_dir + lsSample[i] + "/" + lsSample[i] + "/"        # for linux
        #########################################################
        # file check
        if lsSample[i] not in os.listdir(sSample_dir) :
            print("{0} not in {1}".format(lsSample[i], sSample_dir))
            sys.exit()
        if lsSample[i] + "_ontarget.report" not in os.listdir(sSample_result_dir) :
            print("{0} not in  {1}".format( (lsSample[i] + "_ontarget.report"), sSample_result_dir ))
            sys.exit()
        if lsSample[i] + "_ratio.report" not in os.listdir(sSample_result_dir) :
            print("{0} not in  {1}".format( (lsSample[i] + "_ratio.report"), sSample_result_dir ))
            sys.exit()
        if lsSample[i] + ".sqs" not in os.listdir(sSample_info_dir) :
            print("{0} not in {1}".format( (lsSample[i] + ".sqs"), sSample_info_dir ))
            sys.exit()
        #########################################################
        # file read
        ######### [smaple].sqs
        fSqs = open(sSample_info_dir + lsSample[i] + ".sqs", 'r')
        sGC_ratio = fSqs.readline().split("\t")[4]
        #print("GC_ratio : {0}".format(sGC_ratio))
        #print()
        fSqs.close
        ######### [sample]_ontarget.report
        fOntarget = open(sSample_result_dir + lsSample[i] + "_ontarget.report", 'r')
        lsOntarget_header = fOntarget.readline().strip().split("\t")
        lsOntarget = fOntarget.readline().strip().split("\t")
        #print(lsOntarget_header, len(lsOntarget_header))       # for check
        #print(lsOntarget, len(lsOntarget))     # for check
        #print()
        fOntarget.close()
        ######### [sample]_ratio.report
        fRatio = open(sSample_result_dir + lsSample[i] + "_ratio.report", 'r')
        lsRatio_header = fRatio.readline().strip().split("\t")
        lsRatio = fRatio.readline().strip().split("\t")
        #print(lsRatio_header, len(lsRatio_header))     # for check
        #print(lsRatio, len(lsRatio))       # for check
        #print()
        fRatio.close()
        ###########################################################
        # make liHeader and lsDescription
        for j in range(0, len(lsOntarget_header)) :
            if boolHeader == True : 
                if j == 0 :
                    lsHeader.append(lsOntarget_header[j])
                    lsHeader.append("GC_ratio")
                    lsDescription_sample.append(lsOntarget[j])
                    lsDescription_sample.append(sGC_ratio)
                else :
                    lsHeader.append(lsOntarget_header[j])
                    lsDescription_sample.append(lsOntarget[j])
                if j == len(lsOntarget_header) - 1 :
                    boolHeader == False
            else : break
        for j in range(0, len(lsRatio_header)) :
            lsHeader.append(lsRatio_header[j])
            lsDescription_sample.append(lsRatio[j])
        lsDescription.append(lsDescription_sample)
        #print(lsHeader, len(lsHeader))
        #print(lsDescription, len(lsDescription_sample))
        ###########################################################
        sSample_dir = sSample_dir_ori
    # for loop end
    #if len(lsDescription) == 1 :       # for check
    #    lsDescription.append(lsDescription[0])
    for i in range(0, len(lsHeader)) :
        if (i >= 19 and i <= 40) or (i >= 44 and i <= 47) or i >= 76 : 
                continue
        for j in range(0, len(lsDescription)) :
            if j == 0 :
                fResult.write(lsHeader[i] + "\t" + lsDescription[j][i] + "\t")
            elif j != 0 and j != len(lsDescription) - 1 :
                fResult.write(lsDescription[j][i] + "\t")
            elif j == len(lsDescription) - 1 :
                fResult.write(lsDescription[j][i] + "\n")
        
    fResult.close()



def main() :
    optlist = getopt()
    print(optlist)
    lsSample = []

    #sSample_listFile_dir = "C:\\Users\\shin\\Desktop\\"     # for windows (default)
    sSample_listFile_dir = "/home/shinejh0528/"        # for linux (default)
    
    sAnalysis_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/"    #for linux

    #############################################################
    # parsing optlist
    if len(optlist) == 1 :
        print("Please input option")
        print("1. If has sample_test_report.txt (Default) in {0} : python EnfantGaurd_Analysis_test_report.py [run_id]".format(sSample_listFile_dir))
        print("2. Another file_name : python EnfantGaurd_Analysis_test_report.py [run_id] [sample_list.txt]")
        print("3. samples (more than 2) : python EnfantGaurd_Analysis_test_report.py [run_id] [sample_1] [sample_2] ...")
        sys.exit()
    elif len(optlist) == 2 :
        sRun_ID = optlist[1]
        if "test_report_sample_list.txt" not in os.listdir(sSample_listFile_dir) :
            print("Don't exist 'test_report_sample_list.txt' in {0}".format(sSample_listFile_dir))
            sys.exit()
        fSample_list = open(sSample_listFile_dir + "test_report_sample_list.txt", 'r')
        while True :
            i = fSample_list.readline().strip()
            if i != "" :
                lsSample.append(i.split("\t"))
                print(i)        # for check
            else : break
        fSample_list.close()
    elif len(optlist) == 3 :
        sRun_ID = optlist[1]
        sSample_list_file = optlist[2]
        if "\\" not in sSample_list_file or "/" not in sSample_list_file :
            sSample_list_file = sSample_listFile_dir + sSample_list_file
        fSample_list = open(sSample_list_file, 'r')
        while True :
            i = fSample_list.readline().strip()
            if i != "" :
                lsSample.append(i)
                print(i)        # for check
            else : break
        fSample_list.close()
    elif len(optlist) > 3 :
        sRun_ID = optlist[1]
        for i in range(2, len(optlist)) :
            lsSample.append(optlist[i])      # for check
            print(i)
    #############################################################

    #sSample_dir = sAnalysis_dir + sRun_ID + "\\"        # for windows
    sSample_dir = sAnalysis_dir + sRun_ID + "/"        # for linux

    test_result(sSample_dir, lsSample)
    
main()






