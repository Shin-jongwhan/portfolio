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
                if len(i.split("_")) == 4 : 
                        #if i[:2] == "15" or i[:2] == "16" or i[:2] == "17" or i[:2] == "18" : 
                        #        continue
                        if i[:2] == "19" or i[:2] == "20" : 
                                if "NS" in i or "NB" in i or "NDX" in i :
                                        if os.path.isdir(sFolder_dir + i) : 
                                                lsFolder.append(i)
                                                #print(i)
        
        return lsFolder


def analyze_segment(lsRun_ID, lsDisease_info) : 
        fResult = open("/home/shinejh0528/extract_segment_Joubert_symdrome.txt", 'w')

        lsPrader_Willi = []
        sDisease_name = "16p11.2_microdeletion_syndrome"
        for i in range(0, len(lsDisease_info)) : 
                lsDisease_info[i][0] = lsDisease_info[i][0].replace("chr", "")
                if sDisease_name == lsDisease_info[i][3] : 
                        lsPrader_Willi.append(lsDisease_info[i][:4])
                        #print(lsDisease_info[i][:4])       # for check ['15', '22749354', '28438266', 'Prader-Willi_syndrome']
                        break
        fResult.write("\t".join(lsPrader_Willi[0]) + "\n")
        # if you want to use personal design of segment, use this
        lsPrader_Willi[0] = ['12', '175000', '3875000', '12p13.33_microdeletion_syndrome']
        print(lsPrader_Willi)
        
        fResult = open("/home/shinejh0528/extract_{0}.txt".format(lsPrader_Willi[0][3]), 'w')
        sFolder_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/"
        
        # initialization
        nStart_in = 0
        nEnd_in = 0
        nCover_up = 0
        nSeg_in = 0
        nSample = 0
        # set cutoff
        flGC_ratio_cutoff = 45.00
        nRead_count_cutoff = 1000000
        flOfftarget_MAD_cutoff = 0.3
        flLog_ratio_cutoff = 1

        lsRead_num = []     # for check, num of reads
        boolHeader = True

        for i in range(0, len(lsRun_ID)) : 
                print(lsRun_ID[i])
                for j in os.listdir(sFolder_dir +  lsRun_ID[i] + "/") :     # j == sample_id
                        # ex) j == 2020012838402-EF3-LT
                        sSeg_dir = sFolder_dir + lsRun_ID[i] + "/" + j + "/CopywriteR/CNAprofiles/"
                        sSqs_dir = sFolder_dir + lsRun_ID[i] + "/" + j + "/" + j + "/"      # to get GC rate
                        sSample_dir = sFolder_dir + lsRun_ID[i] + "/" + j + "/"      # to get off-target MAD
                        if os.path.isdir(sFolder_dir + lsRun_ID[i] + "/" + j) : 
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
                                # [sample_ID]_ratio.report
                                if j + "_ratio.report" in os.listdir(sSample_dir) : 
                                        fRatio_report = open(sSample_dir + j + "_ratio.report", 'r')
                                        fRatio_report.readline()       # del first line
                                        sOfftarget_MAD = fRatio_report.readline().split("\t")[6]
                                        #print("Off-target_MAD : {0}".format(sOfftarget_MAD))
                                else : 
                                        print("don't exist {0}_ratio.report in {1}".format(j, sSample_dir))
                                        continue
                                if float(sOfftarget_MAD) > flOfftarget_MAD_cutoff : 
                                        continue
                                fRatio_report.close()
                                ######################################################
                                # check file
                                # [sample_ID]_segment.output.txt
                                if (j + "_segment.output.txt") not in os.listdir(sSeg_dir) : 
                                        #print("don't exist segment.output.txt : {0}".format(j))
                                        continue
                                else : 
                                        fSeg_output = open(sSeg_dir + j + "_segment.output.txt", 'r')
                                        #fSeg_output.readline()      # del header line
                                        lsSeg = []
                                        while True : 
                                                k = fSeg_output.readline().strip()
                                                k = k.replace(chr(34), "")
                                                if k != "" and k != "\n" : 
                                                        #print(k.split("\t"))
                                                        # ex) k.split("\t") == ['37', 'log2.2019060112307.EF3.LT.rmdup.HG19.bam.vs.none', '24', '2675000.5', '28725000.5', '229', '-0.0391']
                                                        lsSeg.append(k.split("\t"))
                                                else : 
                                                        break
                                        fSeg_output.close()
                                        ######################################################
                                        # analysis
                                        sSample_temp = ""
                                        for k in range(0, len(lsSeg)) : 
                                                # lsDisease (lsPrader_Willi) [0] chr_num [1] start [2] end [3] Disease_name
                                                # lsSeg[k] [2] chr_num [3] start [4] end [5] probe [6] log2
                                                #print(lsSeg[k])
                                                #print(lsPrader_Willi[0])
                                                if boolHeader == True : 
                                                        sHeader = "run_id" + "\t" + "\t".join(lsSeg[k][:4]).replace(chr(34), "") + "\t" + "range" + "\t" + "\t".join((lsSeg[k][4:])).replace(chr(34), "")
                                                        fResult.write(sHeader + "\n")
                                                        boolHeader = False
                                                        continue
                                                if boolHeader == False and k == 0 : 
                                                        continue
                                                if ( ( 2 ** ( 1 + float(lsSeg[k][6]) ) ) / 2 ) < flLog_ratio_cutoff : 
                                                        continue
                                                if lsSeg[k][2] == lsPrader_Willi[0][0] : 
                                                        #print(lsSeg[k])
                                                        if ( float(lsPrader_Willi[0][1]) <= float(lsSeg[k][4]) or float(lsPrader_Willi[0][1]) >= float(lsSeg[k][4]) ) and ( float(lsSeg[k][6]) >= 0.25 or float(lsSeg[k][6]) <= -0.25 ) : 
                                                                if (float(lsPrader_Willi[0][1]) <= float(lsSeg[k][3]) and float(lsPrader_Willi[0][2]) > float(lsSeg[k][3]) ) and float(lsPrader_Willi[0][2]) < float(lsSeg[k][4]) : 
                                                                        # segment start in disease region
                                                                        #print(lsSeg[k])
                                                                        nStart_in += 1
                                                                        lsSeg[k][3] = str(int(float(lsSeg[k][3])))
                                                                        lsSeg[k][4] = str(int(float(lsSeg[k][4])))
                                                                        fResult.write( lsRun_ID[i] + "\t" + j + "\t" + "\t".join(lsSeg[k][2:5]) + "\t" + ( str(int(float(lsSeg[k][4]) - float(lsSeg[k][3]))) ) + "\t" + "\t".join(lsSeg[k][5:]) + "\n" )
                                                                        sSample_temp = j
                                                                        continue
                                                                elif ( float(lsPrader_Willi[0][1]) <= float(lsSeg[k][4]) and float(lsPrader_Willi[0][2]) >= float(lsSeg[k][4]) ) and  float(lsPrader_Willi[0][1]) > float(lsSeg[k][3]) : 
                                                                        # segment end in disease region
                                                                        #print(lsSeg[k])
                                                                        nEnd_in += 1
                                                                        lsSeg[k][3] = str(int(float(lsSeg[k][3])))
                                                                        lsSeg[k][4] = str(int(float(lsSeg[k][4])))
                                                                        fResult.write( lsRun_ID[i] + "\t" + j + "\t" + "\t".join(lsSeg[k][2:5]) + "\t" + ( str(int(float(lsSeg[k][4]) - float(lsSeg[k][3]))) ) + "\t" + "\t".join(lsSeg[k][5:]) + "\n" )
                                                                        sSample_temp = j
                                                                        continue
                                                                elif float(lsPrader_Willi[0][1]) >= float(lsSeg[k][3]) and float(lsPrader_Willi[0][2]) <= float(lsSeg[k][4]) : 
                                                                        # segment cover up disease region
                                                                        #print(lsSeg[k])
                                                                        nCover_up += 1
                                                                        lsSeg[k][3] = str(int(float(lsSeg[k][3])))
                                                                        lsSeg[k][4] = str(int(float(lsSeg[k][4])))
                                                                        fResult.write( lsRun_ID[i] + "\t" + j + "\t" + "\t".join(lsSeg[k][2:5]) + "\t" + ( str(int(float(lsSeg[k][4]) - float(lsSeg[k][3]))) ) + "\t" + "\t".join(lsSeg[k][5:]) + "\n" )
                                                                        sSample_temp = j
                                                                        continue
                                                                elif float(lsPrader_Willi[0][1]) <= float(lsSeg[k][3]) and float(lsPrader_Willi[0][2]) >= float(lsSeg[k][4]) : 
                                                                        # segment in disease region
                                                                        #print(lsSeg[k])
                                                                        nSeg_in += 1
                                                                        lsSeg[k][3] = str(int(float(lsSeg[k][3])))
                                                                        lsSeg[k][4] = str(int(float(lsSeg[k][4])))
                                                                        fResult.write( lsRun_ID[i] + "\t" + j + "\t" + "\t".join(lsSeg[k][2:5]) + "\t" + ( str(int(float(lsSeg[k][4]) - float(lsSeg[k][3]))) ) + "\t" + "\t".join(lsSeg[k][5:]) + "\n" )
                                                                        sSample_temp = j
                                                if k == len(lsSeg) - 1 and sSample_temp == j : 
                                                        nSample += 1


                                # else end
                                #print(os.listdir(sSeg_dir))
                #print()
                # for j loop end
        # for i loop end
        fResult.close()
        print("Start_in : {0}, End_in : {1}, Cover_up : {2}, Segment_in : {3}".format(nStart_in, nEnd_in, nCover_up, nSeg_in))
        print("Number of counted sample : {0}".format(nSample))
        
        # for check
        fRead_num = open("/home/shinejh0528/sorted_read_num_{0}.txt".format(lsPrader_Willi[0][3]), 'w')
        lsRead_num = sorted(lsRead_num)
        for i in range(0, len(lsRead_num)) : 
                fRead_num.write(str(lsRead_num[i]) + "\n")
        fRead_num.close()

def main() : 
        #optlist = option()
        lsDisease_info = read_disease_info()
        lsRun_ID = folder_list()
        analyze_segment(lsRun_ID, lsDisease_info)


main()
