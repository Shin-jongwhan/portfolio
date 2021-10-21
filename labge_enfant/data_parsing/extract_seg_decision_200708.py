import sys, getopt
import os
import io


#def option() : 
#        if __name__ == '__main__' : 
#                print(sys, argv)
#                optlist, args = getopt.getopt(sys.argv[1:], 'a:')
#                print("Description : Option (-a [file_name])")
#                print()
#                print(optlist)
#                print()
#
#        return optlist


def read_disease_info() : 
        # ['chrY', '200001', '28000000', 'XYY_syndrome', 'gain', '1.5', '2.5', '1', '1', 'XYY \xec\xa6\x9d\xed\x9b\x84\xea\xb5\xb0', '(XYY syndrome)', 'WD,MO']
        # [0] chr [1] start [2] end [3] disease_name
        file_name = "/data/Analysis/Project/EnfantGuard/info/EnfantGuard.ver3.info"
        fRead = io.open(file_name, 'r')
        lsRead = []

        while True : 
                i = fRead.readline().replace("\n", "")
                if i != "" :
                        lsRead.append(i.encode('utf8').split("\t"))
                else : 
                        break
        
        fRead.close()
        
        ####################################
        # for check
        #print(lsRead[0][0], len(lsRead[0][0]))
        #print(lsRead[-1])
        #print("len(lsRead)", len(lsRead))

        #for i in range(0, len(lsRead)) : 
        #        if "Prader-Willi_syndrome" == lsRead[i][3] : 
        #                print(lsRead[i])
        #                break
        ####################################
        return lsRead
        

def folder_list() : 
        # Run folder list (2019~)
        sFolder_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/"
        lsFolder = []
        for i in os.listdir(sFolder_dir) : 
                if len(i.split("_")) != 4 : 
                        continue
                if "NS" in i or "NB" in i or "NDX" in i :
                        #if i[:2] == "15" or i[:2] == "16" or i[:2] == "17" or i[:2] == "18" : 
                                #continue
                        if os.path.isdir(sRun_dir + i) :
                                lsFolder.append(i)
                                #print(i)
        
        return lsFolder


def analyze_segment(lsRun_ID, lsDisease_info) : 
        lsResult = []
        
        fResult = open("/home/shinejh0528/extract_seg_CNV.txt", 'w')
        sFolder_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/"
        
        # initialization
        nSample = 0
        # set cutoff
        flGC_ratio_cutoff = 45.00
        nRead_count_cutoff = 1000000
        flOfftarget_MAD_cutoff = 0.3
        flLog_ratio_cutoff = 0.8
        lsSearch_range = ["17391543", "17756113"]
        lsResult = []

        lsRead_num = []     # for check, num of reads
        boolHeader = True

        for i in range(0, len(lsRun_ID)) : 
                print(lsRun_ID[i])
                for j in os.listdir(sFolder_dir +  lsRun_ID[i] + "/") :     # j == sample_id
                        sSample = j
                        # ex) j == 2020012838402-EF3-LT
                        sSeg_dir = sFolder_dir + lsRun_ID[i] + "/" + j + "/CopywriteR/CNAprofiles/"
                        sSqs_dir = sFolder_dir + lsRun_ID[i] + "/" + j + "/" + j + "/"      # to get GC rate
                        sSample_dir = sFolder_dir + lsRun_ID[i] + "/" + j + "/"      # to get off-target MAD
                        if os.path.isdir(sFolder_dir + lsRun_ID[i] + "/" + j) : 
                                """
                                ######################################################
                                # check file
                                if "Farther" in j or "Mother" in j or "_" in j : 
                                        continue
                                elif "CopywriteR" not in os.listdir(sSample_dir) : 
                                        continue
                                elif len(j.split("-")[0]) != 13 : 
                                        continue
                                ######################################################
                                # [sample_ID].sqs
                                if j + ".sqs" in os.listdir(sSqs_dir) : 
                                        fSqs = open(sSqs_dir + j + ".sqs", 'r')
                                else : 
                                        print("don't exist {0}.sqs in {1}".format(j, sSqs_dir))
                                        continue
                                sGC_ratio = fSqs.readline().split("\t")[4]
                                #print(sGC_ratio)        # for check
                                if float(sGC_ratio) > flGC_ratio_cutoff : 
                                        continue
                                #print("GC_ratio : {0}".format(sGC_ratio))
                                fSqs.close()
                                ######################################################
                                # [sample_ID].uniq.reads.count
                                if j + ".uniq.reads.count" in os.listdir(sSqs_dir) : 
                                        #print(j)
                                        fRead_count = open(sSqs_dir + j + ".uniq.reads.count", 'r')
                                        fRead_count.readline()      # del first line
                                        sRead_count = fRead_count.readline().strip()
                                        #print(sRead_count)
                                        lsRead_num.append(int(sRead_count))
                                        if int(sRead_count) < nRead_count_cutoff : 
                                                #print(sRead_count)
                                                continue
                                else : 
                                        print("don't exist {0}.uniq.reads.count in {1}".format(j, sSqs_dir))
                                        continue
                                fRead_count.close()
                                ######################################################
                                """
                                # [sample_ID]_ratio.report
                                if j + "_ratio.report" in os.listdir(sSample_dir) : 
                                        fRatio_report = open(sSample_dir + j + "_ratio.report", 'r')
                                        lsRatio_report_header = fRatio_report.readline().split("\t")
                                        #if boolHeader == True : 
                                                #fResult.write("sample\t" + lsRatio_report_header[1] + "\t" + "\t".join(lsRatio_report_header[10:34]) + "\n")
                                                #boolHeader = False
                                        lsRatio_report = fRatio_report.readline().split("\t")
                                        sOfftarget_MAD = lsRatio_report[6]
                                        sSex = lsRatio_report[1]
                                        #lsOfftarget_ratio = lsRatio_report[10:34]
                                        #print("Off-target_MAD : {0}".format(sOfftarget_MAD))
                                        #print(sSex)
                                        #print(lsOfftarget_ratio)
                                else : 
                                        print("don't exist {0}_ratio.report in {1}".format(j, sSample_dir))
                                        continue
                                #if float(sOfftarget_MAD) > flOfftarget_MAD_cutoff : 
                                        #continue
                                if sSex == "female" : 
                                        #print("{0} is female".format(j))
                                        continue
                                fRatio_report.close()
                                ######################################################
                                if j + "_decision_call.result" in os.listdir(sSample_dir) : 
                                        fDecision_call_result = open(sSample_dir + j + "_decision_call.result", 'r')
                                        fDecision_call_result.readline()        # del header
                                        while True : 
                                                k = fDecision_call_result.readline().strip()
                                                if k != "" :
                                                        k = k.split("\t")
                                                        if k[0] == "chrX" : 
                                                                #print(j, k[0], k[1], k[2])
                                                                nOverlap_decision = ( int(k[1]) - int(lsSearch_range[1]) ) * ( int(k[2]) - int(lsSearch_range[0]) )
                                                                #print(nOverlap_decision)
                                                                if nOverlap_decision < 0 and (int(k[2]) - int(k[1])) < 100000000 : 
                                                                        print("sdfasfd", j, k[:6])
                                                                        lsResult.append(k[:6])
                                                                        fResult.write(j + "\t" + "\t".join(k[:6]) + "\n")
                                                else : 
                                                        break
                                        #for i in range(0, len(lsResult)) : 
                                                #print(j)
                                                #fResult.write(j + "\t" + "\t".join(lsResult[i]) + "\n")
                                                #print(lsResult[i])
                                                                        

                                ######################################################


                                nSample += 1
        fResult.close()
        print("Number of counted sample : {0}".format(nSample))
        print("Number of counted sample_male : {0}".format(nSample_male))


def main() : 
        #optlist = option()
        lsDisease_info = read_disease_info()
        lsRun_ID = folder_list()
        analyze_segment(lsRun_ID, lsDisease_info)


main()
