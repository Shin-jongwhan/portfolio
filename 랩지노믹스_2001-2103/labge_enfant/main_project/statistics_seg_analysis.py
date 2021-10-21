#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys, getopt
import os
import io
import time
reload(sys)
sys.setdefaultencoding("utf-8")


def main() : 
        sEnfantGuard_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/"

        fSent_result_DB = open("/home/shinejh0528/enfant_sent_result_DB_all.txt", 'r')
        fSent_result_DB.readline()      # del first line
        lsResult_DB = fSent_result_DB.readlines()
        for i in range(0, len(lsResult_DB)) : 
                lsResult_DB[i] = lsResult_DB[i].strip().split("\t")
        fSent_result_DB.close()
        
        #print(lsResult_DB[0])
        #print(lsResult_DB[0][2])
        
        #fSample_data_result = open("/home/shinejh0528/sample_data_result.txt", 'r')
        #print(fSample_data_result.readline().split("/"))
        #fSample_data_result.close()
        
        flMAD_cutoff = 0.33
        flGC_ratio_cutoff = 46.00
        
        nCorrect_normal = 0
        nIncorrect_normal = 0
        nCorrect_positive = 0
        nIncorrect_positive = 0

        lsCorrect_normal = []
        lsIncorrect_normal = []
        lsCorrect_positive = []
        lsIncorrect_positive = []

        #nNegative_test = 0
        print("len(lsResult_DB) : {0}".format(len(lsResult_DB)))
        for i in range(0, len(lsResult_DB)) : 
                # lsResult_DB[i] : ['180704_NS500435_0500_AHYTKFBGX5', '2018070200624-EF3-LT', '\xec\xa0\x95\xec\x83\x81\xec\x9e\x85\xeb\x8b\x88\xeb\x8b\xa4.']
                sRun = lsResult_DB[i][0]
                sSample = lsResult_DB[i][1]
                sSample_dir = sEnfantGuard_dir + sRun + "/" + sSample + "/"
                sSample_info_dir = sEnfantGuard_dir + sRun + "/" + sSample + "/" + sSample + "/"
                
                #sComment = lsResult_DB[i][2]
                #sComment = u"{0}".format(sComment)
                #print(sComment)
                #if u"정상" in sComment : 
                        #nNegative_test += 1
                        #print(nNegative_test)
                        #print(sComment)
                #print(nNegative_test)      # 15551을 마지막으로 출력해야 하고, 일치 확인

                if os.path.isdir(sSample_dir) == False : 
                        continue
                if os.path.isdir(sSample_info_dir) == False : 
                        continue

                #############################################################
                # check GC ratio in [sSample].sqs
                if sSample + ".sqs" in os.listdir(sSample_info_dir) : 
                        fSqs = open(sSample_info_dir + sSample + ".sqs", 'r')
                else : 
                        print("Don't exist {0}.sqs in {1}".format(sSample, sSample_info_dir))
                        continue
                sGC_ratio = fSqs.readline().split("\t")[4]
                if float(sGC_ratio) > flGC_ratio_cutoff : 
                        print("GC_ratio is above {0} in {1}".format(flGC_ratio_cutoff, sSample))
                        fSqs.close()
                        continue
                fSqs.close()
                #############################################################
                # check MAD in [sSample]_ratio.report
                sOfftarget_MAD = ""
                if sSample + "_ratio.report" in os.listdir(sSample_dir) :
                        fRatio_report = open(sSample_dir + sSample + "_ratio.report", 'r')
                        fRatio_report.readline()        # del first line
                        lsRatio_report = fRatio_report.readline().split("\t")
                        sOfftarget_MAD = lsRatio_report[6]
                else : 
                        print("Don't exist {0}_ratio.report in {1}".format(sSample, sSample_dir))
                        continue
                if float(sOfftarget_MAD) > flMAD_cutoff : 
                        print("Off-target_MAD is above {0} in {1} : {2}".format(flMAD_cutoff, sSample, sOfftarget_MAD))
                        fRatio_report.close()
                        continue
                fRatio_report.close()
                #############################################################
                
                if i != 0 : 
                        if lsResult_DB[i][0] != lsResult_DB[i-1][0] : 
                                os.system("python /home/shinejh0528/seg_analysis_for_statistical_test.py -r {0}".format(lsResult_DB[i][0]))
                #time.sleep(0.5)
                if "sample_data_result.txt" not in os.listdir("/home/shinejh0528/") : 
                        continue
                fSample_data_result = open("/home/shinejh0528/sample_data_result.txt", 'r')
                lsSample_data_result = fSample_data_result.readlines()
                sComment = lsResult_DB[i][2]
                sComment = u"{0}".format(sComment)
                #print("\t".join(lsResult_DB[i]))
                for j in range(0, len(lsSample_data_result)) : 
                        # ['200511_NB501509_0669_AHHWVWBGXF', '2020050219223-EF3-LT', '20200518', '20200502', '19223', 'EF3', 'LT', 'LR', 'NA', '\xec\xa0\x84\xec\x9d\x80\xec\xa7\x80\xec\x95\x84\xea\xb8\xb02', 'NA', 'M', 'KHI', 'Hamilton', 'JHJ']
                        lsSample_data_result[j] = lsSample_data_result[j].strip().split("/")
                        sSample_tmp = lsSample_data_result[j][1]
                        if lsSample_data_result[j][7] != "NA" :
                                sSample_tmp += "-" + lsSample_data_result[j][7]
                        if lsSample_data_result[j][8] != "NA" :
                                sSample_tmp += "-" + lsSample_data_result[j][8]
                        if sSample_tmp == sSample : 
                                #print()
                                #print()
                                print("\t".join(lsResult_DB[i]))
                                print("/".join(lsSample_data_result[j]))
                                if len(lsSample_data_result[j]) == 15 :     # len 15일 경우 음성 
                                        if u"정상" in sComment or "Normal" in sComment :        # 결과 전송 음성, 분석 결과 음성
                                                nCorrect_normal += 1
                                                lsCorrect_normal.append("\t".join(lsResult_DB[i]) + "\t".join(lsSample_data_result[j]))
                                                print("nCorrect_normal {0}".format(nCorrect_normal))
                                        elif u"정상" not in sComment and "Normal" not in sComment :     # 결과 전송 양성인데 분석결과가 음성인 경우
                                                nIncorrect_positive += 1
                                                lsIncorrect_positive.append("\t".join(lsResult_DB[i]) + "\t".join(lsSample_data_result[j]))
                                                print("nIncorrect_positive {0}".format(nIncorrect_positive))
                                elif len(lsSample_data_result[j]) > 15 : 
                                        print("len(lsSample_data_result[j]) : {0}".format(len(lsSample_data_result[j])))
                                        if u"양성" in lsSample_data_result[j][15] : 
                                                if u"정상" in sComment or "Normal" in sComment : 
                                                        continue        # 결과 전송 정상, 분석 결과 양성의심일 경우 continue
                                                else :      # 결과 전송 양성, 분석 결과 양성 의심
                                                        nCorrect_positive += 1
                                                        lsCorrect_positive.append("\t".join(lsResult_DB[i]) + "\t".join(lsSample_data_result[j]))
                                                        print("nCorrect_positive {0}".format(nCorrect_positive))
                                        elif u"음성" in lsSample_data_result[j][15] :
                                                if u"정상" in sComment or "Normal" in sComment :        # 결과 전송 음성, 분석 결과 음성
                                                        nCorrect_normal += 1
                                                        lsCorrect_normal.append("\t".join(lsResult_DB[i]) + "\t".join(lsSample_data_result[j]))
                                                        print("nCorrect_normal {0}".format(nCorrect_normal))
                                                elif u"정상" not in sComment and "Normal" not in sComment :         # 결과 전송 양성, 분석 결과 음성
                                                        nIncorrect_positive += 1
                                                        lsIncorrect_positive.append("\t".join(lsResult_DB[i]) + "\t".join(lsSample_data_result[j]))
                                                        print("nIncorrect_positive {0}".format(nIncorrect_positive))
                # for j loop end
                fSample_data_result.close()
        # for i loop end
        
        fCorrect_normal = open("/home/shinejh0528/statistics_seg_analysis_nega_correct.txt", 'w')
        fCorrect_positive = open("/home/shinejh0528/statistics_seg_analysis_positive_correct.txt", 'w')
        fIncorrect_positive = open("/home/shinejh0528/statistics_seg_analysis_positive_incorrect.txt", 'w')

        for i in range(0, len(lsCorrect_normal)) : 
                fCorrect_normal.write(lsCorrect_normal[i] + "\n")
        for i in range(0, len(lsCorrect_positive)) : 
                fCorrect_positive.write(lsCorrect_positive[i] + "\n")
        for i in range(0, len(lsIncorrect_positive)) : 
                fIncorrect_positive.write(lsIncorrect_positive[i] + "\n")
        
        fCorrect_normal.close()
        fCorrect_positive.close()
        fIncorrect_positive.close()


main()
