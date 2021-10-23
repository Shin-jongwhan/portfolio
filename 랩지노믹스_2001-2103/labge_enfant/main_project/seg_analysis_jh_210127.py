#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys, getopt
import os
import io
import time
import requests
import json,urllib
import datetime
from datetime import datetime as Datetime
print(Datetime.today().strftime("Current time : %Y-%m-%d %H:%M:%S"))

os.environ['http_proxy'] = 'http://192.168.7.12:3128/'
os.environ['https_proxy'] = 'http://192.168.7.12:3128/'
os.environ['ftp_proxy'] = 'http://192.168.7.12:3128/'

key="2C2CB8ED-6D69-457C-981C-8C7CFC24A3E7"

def option() :
        if __name__ == '__main__' :
                print(sys.argv)
                optlist, args = getopt.getopt(sys.argv[1:], 'r:')
                print("Description : python seg_analysis_jh.py -r [Run_ID]")
                print(optlist)
                print("")
                print("")

        return optlist


def read_ISCA_bed() : 
        fISCA = open("/home/shinejh0528/ISCA_180K_Targeted_Regions_hg19.bed", 'r')
        fISCA.readline()        # del first line
        lsISCA = []

        for i in fISCA : 
                i = i.strip().split("\t")
                if i[3] == "Telomere" or i[3] == "Centromere" : 
                        continue
                else : 
                        lsISCA.append(i)
                #if len(i) != 4 :
                #        print(i)       # check done. all len(i) == 4

        fISCA.close()

        return lsISCA


def read_panel_gene_bed() : 
        fPanel_gene = open("/home/shinejh0528/cm_panel.2nd.bed", 'r')
        lsPanel_gene = []

        for i in fPanel_gene : 
                i = i.strip().split("\t")
                lsPanel_gene.append(i)
                #if len(i) != 4 : 
                #        print(i)       # check done. all len(i) == 4

        fPanel_gene.close()

        return lsPanel_gene


def quality_check(sRun_dir, sSample) : 
        sSample_dir = sRun_dir + sSample + "/"
        sSample_info_dir = sRun_dir + sSample + "/" + sSample + "/"
        flMAD_cutoff = 0.3
        flGC_ratio_cutoff = 45.00
        nRead_num_cutoff = 1000000
        flChr_ratio_cutoff = 0.03

        lsOfftarget_ratio = []
        lsChr_ratio_abnormal = []
        
        # initialization
        boolPass = True
        sGC_ratio = ""
        sOfftarget_MAD = ""

        ######################################################################
        # dir and file check
        if len(sSample.split("-")[0]) != 13 or "TEST" in sSample : 
                print("{0} has sample number error OR is test file".format(sSample))
                boolPass = False
                #return False, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD
        if "CopywriteR" not in os.listdir(sSample_dir) : 
                print("Don't exist CopywriteR_dir in {0}".format(sSample_dir))
                boolPass = False
                #return False, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD
        if (sSample + "_segment.output.txt") not in os.listdir(sSample_dir + "CopywriteR/CNAprofiles/") : 
                print("Don't exist {0}_segment.output.txt in {1}CopywriteR/CNAprofiles/".format(sSample,sSample_dir))
                boolPass = False
                #return False, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD
        # Disease_call == 0 check
        if sSample + "_Analysis.result" in os.listdir(sSample_dir) : 
                fAnalysis_result = open(sSample_dir + sSample + "_Analysis.result", 'r')
                lsAnalysis_result = fAnalysis_result.readlines()
                #print(lsAnalysis_result[2].strip())
                if lsAnalysis_result[2].strip().split("\t")[1] != "0" : 
                        print("{0} has disease call : {1}".format(sSample, lsAnalysis_result[2].strip()))
                        #return False
        else : 
                print("Don't exist {0}_Analysis.result in {1}".format(sSample, sSample_dir))
                boolPass = False
                #return False, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD
        fAnalysis_result.close()
        ######################################################################
        # check GC ratio in [sSample].sqs
        if sSample + ".sqs" in os.listdir(sSample_info_dir) : 
                fSqs = open(sSample_info_dir + sSample + ".sqs", 'r')
        else : 
                print("Don't exist {0}.sqs in {1}".format(sSample, sSample_info_dir))
                boolPass = False
                #return False, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD
        sGC_ratio = fSqs.readline().split("\t")[4]
        #print("{0} GC_ratio : {1}".format(sSample, sGC_ratio))     # for check
        if float(sGC_ratio) > flGC_ratio_cutoff : 
                print("GC_ratio is above {0} in {1}".format(flGC_ratio_cutoff, sSample))
                boolPass = False
                #fSqs.close()
                #return False, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD
        fSqs.close()
        ######################################################################
        # check MAD in [sSample]_ratio.report
        if sSample + "_ratio.report" in os.listdir(sSample_dir) : 
                fRatio_report = open(sSample_dir + sSample + "_ratio.report", 'r')
                fRatio_report.readline()        # del first line
                lsRatio_report = fRatio_report.readline().split("\t")
                sOfftarget_MAD = str(round(float(lsRatio_report[6]), 2))
                sSex = lsRatio_report[1]
                lsOfftarget_ratio = lsRatio_report[10:34]
                #print("{0} Off-target_MAD : {1}".format(sSample, sOfftarget_MAD))      #for check
        else : 
                print("Don't exist {0}_ratio.report in {1}".format(sSample, sSample_dir))
                boolPass = False
                #fRatio_report.close()
                #return False, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD
        if float(sOfftarget_MAD) > flMAD_cutoff : 
                print("Off-target_MAD is above {0} in {1} : {2}".format(flMAD_cutoff, sSample, sOfftarget_MAD))
                boolPass = False
                #fRatio_report.close()
                #return False, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD
        for k in range(0, len(lsOfftarget_ratio)) :
                if sSex == "female" :
                        if k == len(lsOfftarget_ratio) - 1 :
                                continue
                        if k != len(lsOfftarget_ratio) - 1 and abs(1.00 - round( float(lsOfftarget_ratio[k]) + 0.001, 2)) > flChr_ratio_cutoff :
                                lsChr_ratio_abnormal.append([ k, str(round(float(lsOfftarget_ratio[k]) + 0.001, 2)) ])
                elif sSex == "male" : 
                        if abs(1.00 - round( float(lsOfftarget_ratio[k]) + 0.001, 2)) > flChr_ratio_cutoff : 
                                lsChr_ratio_abnormal.append([ k, str(round(float(lsOfftarget_ratio[k]) + 0.001, 2)) ])
        if round( float(lsOfftarget_ratio[23]) + 0.001, 2 ) != 0.00 :
                if abs(round( float(lsOfftarget_ratio[22]) + 0.001, 2 ) - round( float(lsOfftarget_ratio[23]) + 0.001, 2 ) ) >= 0.05 : 
                        #print(round( float(lsOfftarget_ratio[22]) + 0.001, 2 ), round( float(lsOfftarget_ratio[23]) + 0.001, 2 ))
                        lsChr_ratio_abnormal.append( ["|X - Y|", str(abs(round( float(lsOfftarget_ratio[22]) + 0.001, 2 ) - round( float(lsOfftarget_ratio[23]) + 0.001, 2 ))) ] )
        fRatio_report.close()
        ######################################################################
        # [sSample].uniq.reads.count
        sRead_count = ""
        if sSample + ".uniq.reads.count" in os.listdir(sSample_info_dir) :
                fRead_count = open(sSample_info_dir + sSample + ".uniq.reads.count", 'r')
                fRead_count.readline()      # del first line
                sRead_count = fRead_count.readline().strip()
                #print("{0} sRead_count : {1}".format(sSample,sRead_count))     # for check
                if int(sRead_count) < nRead_num_cutoff :
                        print("Mapped_reads is below 1000000 in {0}".format(sSample))
                        boolPass = False
                        #fRead_count.close()
                        #return False, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD
        else :
                print("don't exist {0}.uniq.reads.count in {1}".format(sample, sSample_info_dir))
                boolPass = False
                #fRead_count.close()
                #return False, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD
        fRead_count.close()
        ######################################################################
        return boolPass, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD


def read_disease_genes() : 
        ##### if len(lsDisease_genes[i]) != 14
        # chrY  200001  28000000    XYY_syndrome    gain    1.5 2.5 1   1   disease_Korean_language  (XYY syndrome)
        ##### if len(lsDisease_genes[i]) == 14 
        # chrX  147100001   155000000   Xq28_duplication_syndrome   gain    1.25    2.25    1   1   disease_Korean_language    (Xq28 duplication syndrome) GDI1    153665258   153671814
        # lsDisease[i][3] disease name(with under bar) [4] gain, loss [11] gene [12] gene_start [13] gene_end
        fDisease_genes = open("/home/shinejh0528/EnfantGuard_disease_info_genes_200305_jh.txt", 'r')
        lsDisease_genes = []

        while True : 
                i = fDisease_genes.readline().strip()
                if i != "" : 
                        lsDisease_genes.append(i.split("\t"))
                        #print(lsDisease_genes[-1])
                else : 
                        break
        fDisease_genes.close()
        #print("len(lsDisease_genes) : ", len(lsDisease_genes))
        
        #for i in range(0, len(lsDisease_genes)) : # for check
                #print(lsDisease_genes[i])
        return lsDisease_genes


def write_sample(sSample, nLine_num, fWrite) : 
        # write sample name if separated_seg exist and if it don't wrote ever.
        if nLine_num == 0 : 
                fWrite.write(sSample + "\n")
        

def extract_seg(sRun_dir, sSample, fSeparated_seg) : # extract separated segment
        sSeg_dir = sRun_dir + sSample + "/CopywriteR/CNAprofiles/"
        flLog_cutoff = 0.06
        nDup_seg_size_cutoff = 40000       # 100000 = 100 Kb / 40000 = no cutoff
        nDel_seg_size_cutoff = 40000        # 50000 = 50 kb / 40000 = no cutoff
        lsSepa_seg = []     # separated_segment
        
        ######################################################################
        # extract_separacted_segment
        if sSample + "_segment.output.txt" in os.listdir(sSeg_dir) : # file check
                # ex) i.split("\t") : ['"1"', '"log2.2020010414508.EF3.LT.LR.Merged.rmdup.HG19.bam.vs.none"', '1', '775000.5', '249175000.5', '4301', '-0.0059']
                # [2] chr [3] start [4] end [5] probe [6] log
                fSeg_output = open(sSeg_dir + sSample + "_segment.output.txt", 'r')
                fSeg_output.readline()      # del first line

                nLine_num = 0       # write sample name if nLine_num == 0
                while True : 
                        i = fSeg_output.readline().strip()
                        if i != "" : 
                                #print(i.split("\t"))
                                if float(i.split("\t")[6]) > flLog_cutoff and ( float(i.split("\t")[4]) - float(i.split("\t")[3]) ) >= nDup_seg_size_cutoff :
                                        write_sample(sSample, nLine_num, fSeparated_seg)
                                        nLine_num += 1
                                        i_temp = i.split("\t")
                                        i_temp[3] = str(int(float(i_temp[3])))
                                        i_temp[4] = str(int(float(i_temp[4])))
                                        i = "\t".join(i_temp)
                                        lsSepa_seg.append(i.split("\t")[2:])
                                        #print(lsSepa_seg[-1])
                                        fSeparated_seg.write("\t".join(i.split("\t")[2:]) + "\n")
                                elif float(i.split("\t")[6]) < -flLog_cutoff and ( float(i.split("\t")[4]) - float(i.split("\t")[3]) ) >= nDel_seg_size_cutoff :
                                        if i.split("\t")[2] == "15" and int(float(i.split("\t")[4])) < 22749354 :       # 22749354 : Angelman_syndrome start. major noise nearby centromere in relation to An    gelman_syndrome
                                                continue 
                                        else : 
                                                write_sample(sSample, nLine_num, fSeparated_seg)
                                                nLine_num += 1
                                                i_temp = i.split("\t")
                                                i_temp[3] = str(int(float(i_temp[3])))
                                                i_temp[4] = str(int(float(i_temp[4])))
                                                i = "\t".join(i_temp)
                                                lsSepa_seg.append(i.split("\t")[2:])
                                                #print(lsSepa_seg[-1])
                                                fSeparated_seg.write("\t".join(i.split("\t")[2:]) + "\n")
                        else : 
                                break
                fSeg_output.close()
                return True, lsSepa_seg
        else : 
                print("Don't exist {0}_segment.output.txt in {1}".format(sSample, sSeg_dir))
                return False
        ######################################################################


def separated_seg_analysis(sRun_dir, sSample, lsDisease_genes, lsSepa_seg, lsSample_data, lsISCA, lsPanel_gene, fSeg_include_ISCA, lsMicro_disease_info):   # update should be needed
        ### lsSepa_seg
        # ['7', '62625000', '63275000', '4', '-0.5945']
        # [0] chr [1] seg_start [2] seg_end [3] probe [4] log2
        #
        ### lsDisease_genes
        #    if len(lsDisease_genes[i]) != 14
        # chrY  200001  28000000    XYY_syndrome    gain    1.5 2.5 1   1   disease_Korean_language  (XYY syndrome)
        #    if len(lsDisease_genes[i]) == 14
        # chrX  147100001   155000000   Xq28_duplication_syndrome   gain    1.25    2.25    1   1   disease_Korean_language    (Xq28 duplication syndrome) GDI1    153665258   153671814
        # lsDisease[i][3] disease name(with under bar) [4] gain, loss [11] gene [12] gene_start [13] gene_end
        sSample_dir = sRun_dir + sSample + "/"

        ##########################################################
        # disease_call check
        #if sSample + "_Analysis.result" in os.listdir(sSample_dir) : 
        #        fAnalysis_result = open(sSample_dir + sSample + "_Analysis.result", 'r')
        #        lsAnalysis_result = fAnalysis_result.readlines()
        #        #print(lsAnalysis_result[2].strip())
        #        if lsAnalysis_result[2].strip().split("\t")[1] != "0" : 
        #                fAnalysis_result.close()
        #                return lsSample_data
        #else : 
        #        fAnalysis_result.close()
        #        return lsSample_data
        #fAnalysis_result.close()
        ##########################################################
        
        lsSeg_include_ISCA = []
        lsPeri_MicDis_CNV = []


        # convert Num to (chr + Num)
        for i in range(0, 25) : 
                if i < 23 : 
                        for k in range(0, len(lsSepa_seg)) : 
                                if str(i) == lsSepa_seg[k][0] : 
                                        lsSepa_seg[k][0] = "chr%d" % i
                elif i == 23 : 
                        for k in range(0, len(lsSepa_seg)) : 
                                if str(i) == lsSepa_seg[k][0] : 
                                        lsSepa_seg[k][0] = "chrX"
                elif i == 24 : 
                        for k in range(0, len(lsSepa_seg)) : 
                                if str(i) == lsSepa_seg[k][0] : 
                                        lsSepa_seg[k][0] = "chrY"

        #for i in range(0, len(lsSepa_seg)) : 
        #        print(lsSepa_seg[i])
        
        ##############################################################
        # call disease, ISCA
        nLine_num = 0
        lsDisease_call = []
        #sDisease_tmp = ""
        for i in range(0, len(lsSepa_seg)) : 
                #print(lsSepa_seg[i])
                blMicDis = True
                blPeri_MicDis = True
                flSeg_weight = 0.2
                if lsSepa_seg[i][0] == "chrY" : 
                        flSeg_weight = 0.1

                nSeg_size = int(lsSepa_seg[i][2]) - int(lsSepa_seg[i][1])
                if nSeg_size > 1000000 : 
                        flSeg_size = round(float(nSeg_size / 1000000.0), 2)
                        sBase_unit = "Mb"
                elif nSeg_size > 1000 :
                        flSeg_size = int( round(float(nSeg_size / 1000.0), 2) )
                        sBase_unit = "Kb"
                
                # continue FP or almost normal CNV
                if nSeg_size < 500000 and (round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2) > 0.8 and round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2) < 1.3) : 
                        continue
                if nSeg_size < 1000000 and (round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2) > 0.9 and round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2) < 1.15) : 
                        continue
                
                # the segment that have been appeared region often
                if lsSepa_seg[i][0] == 'chr1' and int(lsSepa_seg[i][1]) >= 12875000 and int(lsSepa_seg[i][2]) <= 13775000 : 
                        continue
                if lsSepa_seg[i][0] == 'chr2' and int(lsSepa_seg[i][1]) >= 98025000 and int(lsSepa_seg[i][2]) <= 98175000 :
                        continue
                if lsSepa_seg[i][0] == 'chr14' and int(lsSepa_seg[i][2]) <= 20575000 :
                        continue
                if lsSepa_seg[i][0] == 'chr14' and int(lsSepa_seg[i][1]) > 106000000 :      # terminal, telomere
                        continue
                if lsSepa_seg[i][0] == 'chr15' and int(lsSepa_seg[i][2]) <= 22875000 :
                        continue
                if lsSepa_seg[i][0] == 'chr15' and int(lsSepa_seg[i][2]) <= 24725000 and (round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2) >= 0.8 and round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2) < 1.0) :
                        continue
                if lsSepa_seg[i][0] == 'chr15' and int(lsSepa_seg[i][1]) >= 30375000 and int(lsSepa_seg[i][2]) <= 31075000 : 
                        continue
                
                for k in range(0, len(lsDisease_genes)) : 
                        flCoverage_cutoff = 0.07
                        ##################################################################################
                        # call disease function

                        #print(len(lsDisease_genes[k]))
                        # lsSepa_seg[i][0] chr, [1] seg_start [2] seg_end [3] probe [4] log2
                        # lsDisease_genes[i][0] chr [1] disease_start [2] disease_end [3] disease_name (with underbar) [11] gene [12] gene_S [13] gene_E
                        if lsSepa_seg[i][0] != lsDisease_genes[k][0] : 
                                continue
                        if ( (lsDisease_genes[k][4] == 'gain' and float(lsSepa_seg[i][4]) < 0) or (lsDisease_genes[k][4] == 'loss' and float(lsSepa_seg[i][4]) > 0) ) : 
                                continue

                        #if "2020122826564-EF3-LT" in sSample :
                        #        print("2020122826564-EF3-LT", lsSepa_seg[i])
                        ##################################################################################
                        # peri_MicDis_CNV step1
                        # lsMicro_disease_info is same as lsDisease_genes, [0] chr [1] disease_start [2] disease_end [3] disease_name (with underbar) [11] gene [12] gene_S [13] gene_E
                        # lsPeri_MicDis_CNV [0] seg_chr [1] seg_S [2] seg_E [3] seg_CNV [4] seg_range [5] sBase_unit(Kb or Mb) [6] disease_name (with underbar)
                        #nAdd_peri_MicDis_range = 1000000
                        #blReEnter_peri_MicDis = False
                        #nPeri_MicDis_S = -1     # initialization, if -1, then don't execute.
                        #nPeri_MicDis_E = -1     # initialization, if -1, then don't execute.
                        #for j in range(0, len(lsMicro_disease_info)) : 
                        #        if lsMicro_disease_info[j][3] == lsDisease_genes[k][3] : 
                        #                nPeri_MicDis_S = int(lsMicro_disease_info[j][1]) - nAdd_peri_MicDis_range
                        #                nPeri_MicDis_E = int(lsMicro_disease_info[j][2]) + nAdd_peri_MicDis_range
                        #                #if nPeri_MicDis < 0 : 
                        #                #        nPeri_MicDis = 0       # Don't matter on this func
                        #                break
                        #
                        #if lsPeri_MicDis_CNV == [] :         # check whether or not same disease entered
                        #        None
                        #elif lsPeri_MicDis_CNV[-1][6] == lsDisease_genes[k][3] : 
                        #        #print("True {0}, {1}\n\n\n".format(lsPeri_MicDis_CNV[-1][6], lsDisease_genes[k][3]))
                        #        blReEnter_peri_MicDis = True
                        #elif lsPeri_MicDis_CNV[-1][6] != lsDisease_genes[k][3] :
                        #        blReEnter_peri_MicDis = False
                        #
                        #if nPeri_MicDis_S != -1 and blReEnter_peri_MicDis == False : 
                        #        blSeg_overlap_ptc_above_cutoff = False
                        #        # often have been appeared region
                        #        if ( int(lsSepa_seg[i][1]) >= int(lsDisease_genes[k][1]) and int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][2]) ) or ( int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][1]) and int(lsSepa_seg[i][2]) >= int(lsDisease_genes[k][1]) ) : 
                        #                nOverlap_start = max( int(lsSepa_seg[i][1]), int(lsDisease_genes[k][1]) )
                        #                nOverlap_end = min( int(lsSepa_seg[i][2]), int(lsDisease_genes[k][2]) )
                        #                nOverlap_size = nOverlap_end - nOverlap_start
                        #                nDisease_size = int(lsDisease_genes[k][2]) - int(lsDisease_genes[k][1])
                        #                flOverlap_ptc = round(( float(nOverlap_size) / float(nDisease_size) ), 2)
                        #                if flOverlap_ptc > flCoverage_cutoff : 
                        #                        blSeg_overlap_ptc_above_cutoff = True
                        #                None        # skip if seg in disease range
                        #        if blSeg_overlap_ptc_above_cutoff == False and ( int(lsSepa_seg[i][1]) >= nPeri_MicDis_S and int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][1]) ) or ( int(lsSepa_seg[i][1]) <= nPeri_MicDis_S and int(lsSepa_seg[i][2]) >= nPeri_MicDis_S ) :         # append if seg in peri_MicDis
                        #                lsPeri_MicDis_CNV.append([ lsSepa_seg[i][0], lsSepa_seg[i][1], lsSepa_seg[i][2], str(round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2)), str(flSeg_size), sBase_unit, lsMicro_disease_info[j][3] ])
                        #                #print(lsPeri_MicDis_CNV[-1][6], lsDisease_genes[k][3])
                        #                #print("Peri_MicDis_CNV : {0}\n\n\n".format(lsPeri_MicDis_CNV[-1]))
                        #        if blSeg_overlap_ptc_above_cutoff == False and ( int(lsSepa_seg[i][1]) >= int(lsDisease_genes[k][2]) and int(lsSepa_seg[i][1]) <= nPeri_MicDis_E ) or ( int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][2]) and int(lsSepa_seg[i][2]) >= int(lsDisease_genes[k][2]) ) :         # append if seg in peri_MicDis
                        #                lsPeri_MicDis_CNV.append([ lsSepa_seg[i][0], lsSepa_seg[i][1], lsSepa_seg[i][2], str(round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2)), str(flSeg_size), sBase_unit, lsMicro_disease_info[j][3] ])
                        #                #print(lsPeri_MicDis_CNV[-1][6], lsDisease_genes[k][3])
                        #                #print("Peri_MicDis_CNV : {0}\n\n\n".format(lsPeri_MicDis_CNV[-1]))
                        #
                        # peri_MicDis_CNV step 1 end
                        ##################################################################################
                        if ( int(lsSepa_seg[i][1]) >= int(lsDisease_genes[k][1]) and int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][2]) ) or ( int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][1]) and int(lsSepa_seg[i][2]) >= int(lsDisease_genes[k][1]) ) :   # identical chr, gain or loss, overlapped
                                nOverlap_start = max( int(lsSepa_seg[i][1]), int(lsDisease_genes[k][1]) )
                                nOverlap_end = min( int(lsSepa_seg[i][2]), int(lsDisease_genes[k][2]) )
                                nOverlap_size = nOverlap_end - nOverlap_start
                                nDisease_size = int(lsDisease_genes[k][2]) - int(lsDisease_genes[k][1])
                                flOverlap_ptc = round(( float(nOverlap_size) / float(nDisease_size) ), 2)
                                if flOverlap_ptc > flCoverage_cutoff and int(lsSepa_seg[i][3]) > ( ( float(lsSepa_seg[i][2]) - float(lsSepa_seg[i][1]) ) / 50000 ) * flSeg_weight : 
                                        #lsDisease_call
                                        #[0] chr [1] seg_S [2] seg_E [3] CNV [4] size ([5] probe) [6] disease (with underbar) [7] "[overlap_ptc]% overlapped"
                                        lsDisease_call.append(lsSepa_seg[i][:3])
                                        lsDisease_call[-1].append(str(round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2)))     # CNV
                                        if sBase_unit == "Kb" : 
                                                lsDisease_call[-1].append(str( int(flSeg_size) ) + " " + sBase_unit)
                                        else : 
                                                lsDisease_call[-1].append(str( flSeg_size ) + " " + sBase_unit)
                                        lsDisease_call[-1].append(lsSepa_seg[i][3]) # probe
                                        lsDisease_call[-1].append(lsDisease_genes[k][3])
                                        lsDisease_call[-1].append("{0}% overlapped".format(str(flOverlap_ptc * 100)))
                                        lsDisease_call[-1].append(lsDisease_genes[k][1])
                                        lsDisease_call[-1].append(lsDisease_genes[k][2])
                                        print("\t".join(lsDisease_call[-1]))

                                        blMicDis = False
                                        blPeri_MicDis = False
                                if len(lsDisease_genes[k]) == 11 : 
                                        continue
                                if ( int(lsSepa_seg[i][1]) >= int(lsDisease_genes[k][12]) and int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][13]) ) or ( int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][12]) and int(lsSepa_seg[i][2]) >= int(lsDisease_genes[k][12]) ) :     # if seg in gene region
                                        #[0] chr [1] seg_S [2] seg_E [3] CNV [4] size ([5] probe) [6] disease (with underbar) [7] gene
                                        lsDisease_call.append(lsSepa_seg[i][:3])
                                        lsDisease_call[-1].append(str(round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2)))     # CNV
                                        lsDisease_call[-1].append(str( flSeg_size ) + " " + sBase_unit)
                                        lsDisease_call[-1].append(lsSepa_seg[i][3]) # probe
                                        lsDisease_call[-1].append(lsDisease_genes[k][3])
                                        lsDisease_call[-1].append(lsDisease_genes[k][11])
                                        lsDisease_call[-1].append(lsDisease_genes[k][1])
                                        lsDisease_call[-1].append(lsDisease_genes[k][2])
                                        print("\t".join(lsDisease_call[-1]))

                                        blMicDis = False
                                        blPeri_MicDis = False
                        # call disease function end
                        ############################################################################################
                        # peri_MicDis_CNV step1
                        # lsMicro_disease_info is same as lsDisease_genes, [0] chr [1] disease_start [2] disease_end [3] disease_name (with underbar) [11] gene [12] gene_S [13] gene_E
                        # lsPeri_MicDis_CNV [0] seg_chr [1] seg_S [2] seg_E [3] seg_CNV [4] seg_range [5] sBase_unit(Kb or Mb) [6] disease_name (with underbar)
                        nAdd_peri_MicDis_range = 1000000
                        blReEnter_peri_MicDis = False
                        nPeri_MicDis_S = -1     # initialization, if -1, then don't execute.
                        nPeri_MicDis_E = -1     # initialization, if -1, then don't execute.
                        for j in range(0, len(lsMicro_disease_info)) :
                                if lsMicro_disease_info[j][3] == lsDisease_genes[k][3] :
                                        nPeri_MicDis_S = int(lsMicro_disease_info[j][1]) - nAdd_peri_MicDis_range
                                        nPeri_MicDis_E = int(lsMicro_disease_info[j][2]) + nAdd_peri_MicDis_range
                                        #if nPeri_MicDis < 0 :
                                        #        nPeri_MicDis = 0       # Don't matter on this func
                                        break

                        if lsPeri_MicDis_CNV == [] :         # check whether or not same disease entered
                                None
                        elif lsPeri_MicDis_CNV[-1][6] == lsDisease_genes[k][3] :
                                #print("True {0}, {1}\n\n\n".format(lsPeri_MicDis_CNV[-1][6], lsDisease_genes[k][3]))
                                blReEnter_peri_MicDis = True
                        elif lsPeri_MicDis_CNV[-1][6] != lsDisease_genes[k][3] :
                                blReEnter_peri_MicDis = False

                        if blPeri_MicDis == True :      # skip if segment have got seg_analysis issue
                                None
                        elif nPeri_MicDis_S != -1 and blReEnter_peri_MicDis == False :
                                blSeg_overlap_ptc_above_cutoff = False
                                # often have been appeared region
                                if ( int(lsSepa_seg[i][1]) >= int(lsDisease_genes[k][1]) and int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][2]) ) or ( int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][1]) and int(lsSepa_seg[i][2]) >= int(lsDisease_genes[k][1]) ) :
                                        nOverlap_start = max( int(lsSepa_seg[i][1]), int(lsDisease_genes[k][1]) )
                                        nOverlap_end = min( int(lsSepa_seg[i][2]), int(lsDisease_genes[k][2]) )
                                        nOverlap_size = nOverlap_end - nOverlap_start
                                        nDisease_size = int(lsDisease_genes[k][2]) - int(lsDisease_genes[k][1])
                                        flOverlap_ptc = round(( float(nOverlap_size) / float(nDisease_size) ), 2)
                                        if flOverlap_ptc > flCoverage_cutoff :
                                                blSeg_overlap_ptc_above_cutoff = True
                                        None        # skip if seg in disease range
                                if blSeg_overlap_ptc_above_cutoff == False and ( int(lsSepa_seg[i][1]) >= nPeri_MicDis_S and int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][1]) ) or ( int(lsSepa_seg[i][1]) <= nPeri_MicDis_S and int(lsSepa_seg[i][2]) >= nPeri_MicDis_S ) :         # append if seg in peri_MicDis
                                        lsPeri_MicDis_CNV.append([ lsSepa_seg[i][0], lsSepa_seg[i][1], lsSepa_seg[i][2], str(round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2)), str(flSeg_size), sBase_unit, lsMicro_disease_info[j][3] ])
                                        #print(lsPeri_MicDis_CNV[-1][6], lsDisease_genes[k][3])
                                        #print("Peri_MicDis_CNV : {0}\n\n\n".format(lsPeri_MicDis_CNV[-1]))
                                if blSeg_overlap_ptc_above_cutoff == False and ( int(lsSepa_seg[i][1]) >= int(lsDisease_genes[k][2]) and int(lsSepa_seg[i][1]) <= nPeri_MicDis_E ) or ( int(lsSepa_seg[i][1]) <= int(lsDisease_genes[k][2]) and int(lsSepa_seg[i][2]) >= int(lsDisease_genes[k][2]) ) :         # append if seg in peri_MicDis
                                        lsPeri_MicDis_CNV.append([ lsSepa_seg[i][0], lsSepa_seg[i][1], lsSepa_seg[i][2], str(round( (2 ** (1 + float(lsSepa_seg[i][4]))) / 2, 2)), str(flSeg_size), sBase_unit, lsMicro_disease_info[j][3] ])
                                        #print(lsPeri_MicDis_CNV[-1][6], lsDisease_genes[k][3])
                                        #print("Peri_MicDis_CNV : {0}\n\n\n".format(lsPeri_MicDis_CNV[-1]))

                        # peri_MicDis_CNV step 1 end
                        ##############################################################################################




                #for k loop end
                #########################################################################################
                # call ISCA
                # lsSepa_seg[i][0] chr, [1] seg_start [2] seg_end [3] probe
                # lsISCA[j] [0] chr [1] start [2] end [3] gene_name
                for j in range(0, len(lsISCA)) : 
                        if lsSepa_seg[i][0] != lsISCA[j][0] :       # if not ideltical chr, continue
                                continue
                        if round(float(2.0 ** float(lsSepa_seg[i][4])), 2) >= 0.8 and round(float(2.0 ** float(lsSepa_seg[i][4])), 2) <= 1.2 : 
                                break
                        if ( int(lsSepa_seg[i][1]) >= int(lsISCA[j][1]) and int(lsSepa_seg[i][1]) <= int(lsISCA[j][2]) ) or ( int(lsSepa_seg[i][1]) <= int(lsISCA[j][2]) and int(lsSepa_seg[i][2]) >= int(lsISCA[j][1]) ) or ( int(lsSepa_seg[i][1]) <= int(lsISCA[j][1]) and int(lsSepa_seg[i][2]) >= int(lsISCA[j][2]) ) :   # if segment overlapped
                                #lsSeg_include_ISCA_tmp = lsSepa_seg[i] + lsISCA[j]
                                #lsSeg_include_ISCA.append(lsSeg_include_ISCA_tmp)
                                nSeg_size = int(lsSepa_seg[i][2]) - int(lsSepa_seg[i][1])
                                if round(float(2.0 ** float(lsSepa_seg[i][4])), 2) > 1 : 
                                        sDup_or_del = "Dup"
                                else : 
                                        sDup_or_del = "Del"
                                lsSeg_include_ISCA.append(lsSepa_seg[i] + lsISCA[j])
                                for k in range(0, len(lsSample_data)) :
                                        sSample_tmp = lsSample_data[k][1]
                                        if lsSample_data[k][7] != "NA" :
                                                sSample_tmp += "-" + lsSample_data[k][7]
                                        if lsSample_data[k][8] != "NA" : 
                                                sSample_tmp += "-" + lsSample_data[k][8]
                                        elif lsSample_data[k][8] != "NA" and lsSample_data[k][8] == lsSample_data[k][7] :
                                                sSample_tmp += "2"      # LR2 or SR2
                                        if sSample_tmp == sSample : 
                                                print("ISCA : {0}\t{1}\t{2}\t{3}:{4}-{5}\t{6}\t{7} {8}\t{9}\t{10}\n".format( sRun_dir.split("/")[-2], sSample, lsSample_data[k][9], lsSepa_seg[i][0], '{0:,}'.format(int(lsSepa_seg[i][1])), '{0:,}'.format(int(lsSepa_seg[i][2])), round(float(2.0 ** float(lsSepa_seg[i][4])), 2), str(flSeg_size), sBase_unit, sDup_or_del, lsISCA[j][3]) )
                                                fSeg_include_ISCA.write("{0}\t{1}\t{2}\t{3}:{4}-{5}\t{6}\t{7} {8}\t{9}\t{10}\n".format( sRun_dir.split("/")[-2], sSample, lsSample_data[k][9], lsSepa_seg[i][0], '{0:,}'.format(int(lsSepa_seg[i][1])), '{0:,}'.format(int(lsSepa_seg[i][2])), round(float(2.0 ** float(lsSepa_seg[i][4])), 2), str(flSeg_size), sBase_unit, sDup_or_del, lsISCA[j][3]) )
                # call ISCA end
                #########################################################################################
                # call MicDis
                for k in range(0, len(lsMicro_disease_info)) : 
                        # lsSepa_seg[i][0] chr, [1] seg_start [2] seg_end [3] probe
                        # lsMicro_disease_info [0] chr [1] start [2] end [3] disease with underbar [4] 'gain' or 'loss'
                        # ['chrX', '147100001', '155000000', 'Xq28_duplication_syndrome', 'gain', '1.25', '2.25', '1', '1', 'Xq28 \xec\xa4\x91\xeb\xb3\xb5 \xec\xa6\x9d\xed\x9b\x84\xea\xb5\xb0', '(Xq28 duplication syndrome)']

                        if blMicDis == False :      # skip if already segment call have done
                                break
                        if lsSepa_seg[i][0] != lsMicro_disease_info[k][0] : 
                                continue
                        if round(float(2.0 ** float(lsSepa_seg[i][4])), 2) < 1 and lsMicro_disease_info[k][4] == 'gain' : 
                                continue
                        elif round(float(2.0 ** float(lsSepa_seg[i][4])), 2) > 1 and lsMicro_disease_info[k][4] == 'loss' :
                                continue

                        if ( int(lsSepa_seg[i][1]) <= int(lsMicro_disease_info[k][1]) and int(lsSepa_seg[i][2]) >= int(lsMicro_disease_info[k][1]) ) or ( int(lsSepa_seg[i][1]) >= int(lsMicro_disease_info[k][1]) and int(lsSepa_seg[i][1]) <= int(lsMicro_disease_info[k][2]) ) : 
                                print(lsSepa_seg[i], lsMicro_disease_info[k][:4])
                                #       |------------------------| MicDis
                                # |------------------------------------------> seg
                                #           |--------------------------------> seg
                                for j in range(0, len(lsSample_data)) :
                                        sSample_tmp = lsSample_data[j][1]
                                        if lsSample_data[j][7] != "NA" :
                                                sSample_tmp += "-" + lsSample_data[j][7]
                                        if lsSample_data[j][8] != "NA" and lsSample_data[j][8] == lsSample_data[j][7] :
                                                sSample_tmp += "2"      # LR2 or SR2
                                        elif lsSample_data[j][8] != "NA" :
                                                sSample_tmp += "-" + lsSample_data[j][8]
                                        if sSample == sSample_tmp :
                                                sIssue_tmp = "'검토 요망 {0}:{1}-{2} CNV {3}  {4} {5}  {6}'".format( str(lsSepa_seg[i][0]), '{0:,}'.format(int(lsSepa_seg[i][1])), '{0:,}'.format(int(lsSepa_seg[i][2])), round(float(2.0 ** float(lsSepa_seg[i][4])), 2), flSeg_size, sBase_unit, lsMicro_disease_info[k][3] )
                                                if len(lsSample_data[j]) == 15 :
                                                        lsSample_data[j].append("")
                                                        lsSample_data[j].append("")
                                                        lsSample_data[j].append("")
                                                        lsSample_data[j].append("")
                                                        lsSample_data[j].append(sIssue_tmp)
                                                elif len(lsSample_data[j]) == 16 : 
                                                        lsSample_data[j].append("")
                                                        lsSample_data[j].append("")
                                                        lsSample_data[j].append("")
                                                        lsSample_data[j].append(sIssue_tmp)
                                                elif len(lsSample_data[j]) == 17 :
                                                        lsSample_data[j].append("")
                                                        lsSample_data[j].append("")
                                                        lsSample_data[j].append(", " + sIssue_tmp)
                                                elif len(lsSample_data[j]) == 18 : 
                                                        lsSample_data[j].append("")
                                                        lsSample_data[j].append(", " + sIssue_tmp)
                                                elif len(lsSample_data[j]) == 19 :
                                                        lsSample_data[j].append(", " + sIssue_tmp)
                                                elif len(lsSample_data[j]) == 20 :
                                                        lsSample_data[j][19] = lsSample_data[j][19] + ", " + sIssue_tmp
                # call MicDis end
                #for k loop end
                #########################################################################################
                        
        # for i loop end
        ##############################################################################
        # peri_MicDis_CNV step 2 : lsPeri_MicDis parsing
        # lsPeri_MicDis_CNV[i][0] seg_chr, [1] seg_S [2] seg_E [3] CNV [4] range [5] sBase_unit (Kb or Mb) [6] disease_with_under_bar
        if lsPeri_MicDis_CNV != [] or len(lsPeri_MicDis_CNV) == 1 : 
                for i in range(len(lsPeri_MicDis_CNV) - 1, 0, -1) : 
                        if lsPeri_MicDis_CNV[i][0] == lsPeri_MicDis_CNV[i - 1][0] and lsPeri_MicDis_CNV[i][1] == lsPeri_MicDis_CNV[i - 1][1] and lsPeri_MicDis_CNV[i][2] == lsPeri_MicDis_CNV[i - 1][2] :       # if seg_chr, S, E is same, del a list[i] and add disease name to [i - 1]
                                lsPeri_MicDis_CNV[i - 1][6] += ", {0}".format(lsPeri_MicDis_CNV[i][6])
                                del lsPeri_MicDis_CNV[i]
                for i in range(0, len(lsPeri_MicDis_CNV)) : 
                        print("peri_MicDis_CNV : {0}:{1}-{2} CNV {3} {4}{5} {6} 주변".format(lsPeri_MicDis_CNV[i][0], lsPeri_MicDis_CNV[i][1], lsPeri_MicDis_CNV[i][2], lsPeri_MicDis_CNV[i][3], lsPeri_MicDis_CNV[i][4], lsPeri_MicDis_CNV[i][5], lsPeri_MicDis_CNV[i][6]))


        # peri_MicDis_CNV step 2 : lsPeri_MicDis_parsing end
        ##########################################################
        # write positive
        # lsSample_data, len(lsSample_data) == 15 or 17 or 20
        # [0] run_id [1] sample [2] date_of_first_report [3] date_of_upload [4]sample_branch [5] EF3 [6] LT [7] NA or LR or SR [8] Merged or else [9] initial
        # [15] 음성 / 양성 [16] disease [19] issue
        if sSample + "_Analysis.result" in os.listdir(sSample_dir) :        # Disease_call check
                fAnalysis_result = open(sSample_dir + sSample + "_Analysis.result", 'r')
                lsAnalysis_result = fAnalysis_result.readlines()        # lsAnalysis_result[2].strip().split("\t")[1] : Disease_call num
                fAnalysis_result.close()
        for i in range(0, len(lsSample_data)) : 
                sSample_tmp = lsSample_data[i][1]
                if lsSample_data[i][7] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][7]
                if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] :
                        sSample_tmp += "2"      # LR2 or SR2
                elif lsSample_data[i][8] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][8]
                if sSample_tmp == sSample and lsDisease_call != [] : 
                        for j in range(len(lsDisease_call) - 1, -1, -1) : 
                                nIdentical_entry = 0
                                for k in range(0, len(lsDisease_call)) : 
                                        if "".join(lsDisease_call[j]) == "".join(lsDisease_call[k]) : 
                                                nIdentical_entry += 1
                                                if nIdentical_entry > 1 : 
                                                        del lsDisease_call[j]
                                                        break
                        for j in range(0, len(lsDisease_call)) :
                                #lsDisease_call
                                #[0] chr [1] seg_S [2] seg_E [3] CNV [4] size [5] probe [6] disease (with underbar) [7] gene or overlap_pct [8] disease_S [9] disease_E
                                sDisease_region_tmp = lsDisease_call[j][0] + ":" + '{0:,}'.format(int(lsDisease_call[j][1])) + "-" + '{0:,}'.format(int(lsDisease_call[j][2])) + "  CNV " +  " ".join(lsDisease_call[j][3:5])

                                if int(lsDisease_call[j][9]) - int(lsDisease_call[j][8]) > 1000000 and int(lsDisease_call[j][9]) - int(lsDisease_call[j][8]) < 5000000 : 
                                        sDisease_region_tmp += "  disease range:" + str( round( float(int(lsDisease_call[j][9]) - int(lsDisease_call[j][8])) / 1000000, 2) ) + " Mb"
                                elif int(lsDisease_call[j][9]) - int(lsDisease_call[j][8]) <= 1000000 : 
                                        sDisease_region_tmp += "  disease range:" + str( round( float(int(lsDisease_call[j][9]) - int(lsDisease_call[j][8])) / 1000, 2) ) + " Kb"

                                sIssue_tmp = sDisease_region_tmp + "    " + " ".join(lsDisease_call[j][6:8])

                                if len(lsSample_data[i]) == 15 : 
                                        lsSample_data[i].append("양성 의심??")
                                        lsSample_data[i].append(lsDisease_call[j][6])
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append(sIssue_tmp)
                                elif len(lsSample_data[i]) == 17 : 
                                        if lsDisease_call[j][6] not in lsSample_data[i][16] and lsAnalysis_result[2].strip().split("\t")[1] == "0" : 
                                                lsSample_data[i][16] = lsSample_data[i][16] + ", " + lsDisease_call[j][6]
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append(sIssue_tmp)
                                elif len(lsSample_data[i]) == 20 : 
                                        if lsSample_data[i][15] == "" : 
                                                lsSample_data[i][15] = "양성 의심??"
                                        if lsDisease_call[j][6] not in lsSample_data[i][16] and lsAnalysis_result[2].strip().split("\t")[1] == "0" :
                                                if lsSample_data[i][16] != "" : 
                                                        lsSample_data[i][16] = lsSample_data[i][16] + ", " + lsDisease_call[j][6]
                                                else : 
                                                        lsSample_data[i][16] = lsDisease_call[j][6]
                                        if sDisease_region_tmp not in lsSample_data[i][19] :
                                        #if sDisease_region_tmp not in sIssue_tmp :
                                                lsSample_data[i][19] = lsSample_data[i][19] + ", " + sIssue_tmp
                                        elif sDisease_region_tmp in lsSample_data[i][19] and lsDisease_call[j][6] not in lsSample_data[i][19] : 
                                        #elif sDisease_region_tmp in sIssue_tmp and lsDisease_call[j][6] not in lsSample_data[i][19] : 
                                                lsSample_data[i][19] = lsSample_data[i][19] + ", " + " ".join(lsDisease_call[j][6:8])
                                        elif sDisease_region_tmp in lsSample_data[i][19] and lsDisease_call[j][6] in lsSample_data[i][19] and lsDisease_call[j][7] not in lsSample_data[i][19]  : 
                                        #elif sDisease_region_tmp in sIssue_tmp and lsDisease_call[j][6] in lsSample_data[i][19] :       # gene
                                                lsSample_data[i][19] = lsSample_data[i][19] + ", " + lsDisease_call[j][7]
                                        else : 
                                                lsSample_data[i][19] = lsSample_data[i][19] + ", " + sIssue_tmp
        # write positive end
        ##########################################################

        return lsSample_data, lsPeri_MicDis_CNV


                        
def samplesheet_py(sRun_ID) : 
        os.system("python /home/shinejh0528/samplesheet_jh.py {0}".format(sRun_ID))
        time.sleep(1)       # to avoid error the file wouldn't be created.
        fSample_data = open("/home/shinejh0528/sample_data.txt".format(sRun_ID), 'r')
        lsSample_data = []
        while True : 
                i = fSample_data.readline()
                if i != "" : 
                        lsSample_data.append(i.strip().split("/"))
                else : 
                        break
        fSample_data.close()
        #print("lsSample_data")
        #for i in range(0, len(lsSample_data)) : 
        #        print(lsSample_data[i])
        return lsSample_data


def append_disease_call_in_lsSample_data(lsSample_data, sRun_dir, sSample) : 
        sSample_dir = sRun_dir + sSample + "/"
        if sSample + "_Analysis.result" in os.listdir(sSample_dir) : 
                fAnalysis_result = open(sSample_dir + sSample + "_Analysis.result", 'r')
                lsAnalysis_result = fAnalysis_result.readlines()
                if lsAnalysis_result[2].strip().split("\t")[1] == "0" : 
                        fAnalysis_result.close()
                        return lsSample_data
        for i in range(0, len(lsSample_data)) : 
                sSample_tmp = lsSample_data[i][1]
                if lsSample_data[i][7] != "NA" : 
                        sSample_tmp += "-" + lsSample_data[i][7]
                if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] :
                        sSample_tmp += "2"      # LR2 or SR2
                elif lsSample_data[i][8] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][8]
                if sSample == sSample_tmp : 
                        if sSample + "_decision_call.result" in os.listdir(sSample_dir) : 
                                fDecision_call_result = open(sSample_dir + sSample + "_decision_call.result", 'r')
                                fDecision_call_result.readline()        # del header
                                while True : 
                                        k = fDecision_call_result.readline().strip()
                                        if k != "" : 
                                                k = k.split("\t")
                                                if k[9] != "" : 
                                                        if len(lsSample_data[i]) < 16 : 
                                                                lsSample_data[i].append("양성 콜")
                                                                lsSample_data[i].append(k[9])
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("")
                                                                #lsSample_data[i].append("양성 콜 {0}".format(k[9]))
                                                                lsSample_data[i].append("양성 콜")
                                                        else : 
                                                                if k[9] not in lsSample_data[i][16] : 
                                                                        lsSample_data[i][16] += ", {0}".format(k[9])
                                        else : 
                                                if len(lsSample_data[i]) > 16 : 
                                                        print("/".join(lsSample_data[i]))
                                                break
                                fDecision_call_result.close()
                        else : 
                                print("Don't exist {0}_decision_call.result".format(sSample))

        return lsSample_data


def append_negative_in_lsSample_data(lsSample_data,sRun_dir, sSample) : 
        # write negative if the sample pass disease_call algorithm and has nothing in disease_call.result
        sSample_dir = sRun_dir + sSample + "/"
        if sSample + "_Analysis.result" in os.listdir(sSample_dir) :
                fAnalysis_result = open(sSample_dir + sSample + "_Analysis.result", 'r')
                lsAnalysis_result = fAnalysis_result.readlines()
                if lsAnalysis_result[2].strip().split("\t")[1] != "0" :
                        return lsSample_data
        fAnalysis_result.close()
        nLine_num = 0
        for i in range(0, len(lsSample_data)) :
                sSample_tmp = lsSample_data[i][1]
                if lsSample_data[i][7] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][7]
                if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] :
                        sSample_tmp += "2"      # LR2 or SR2
                elif lsSample_data[i][8] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][8]
                if sSample == sSample_tmp :
                        if sSample + "_decision_call.result" in os.listdir(sSample_dir) :
                                fDecision_call_result = open(sSample_dir + sSample + "_decision_call.result", 'r')
                                fDecision_call_result.readline()        # del header
                                while True :
                                        k = fDecision_call_result.readline().strip()
                                        #print(k)
                                        if k != "" : 
                                                nLine_num += 1
                                        elif k == "" and nLine_num == 0 : 
                                                if len(lsSample_data[i]) == 15 : 
                                                        lsSample_data[i].append("음성")
                                                break
                                        elif k == "" and nLine_num != 0 : 
                                                break
                                fDecision_call_result.close()
                        else : 
                                print("Don't exist {0}_decision_call.result".format(sSample))
        # for loop end
        return lsSample_data


def issue_call(lsSample_data, sRun_dir, sSample) : 
        # write isuue
        # 1. Mapped yield 2. sex coincidence
        sSample_dir = sRun_dir + sSample + "/"
        if sSample + "_issue.report" in os.listdir(sSample_dir) : 
                fIssue_report = open(sSample_dir + sSample + "_issue.report", 'r')
                lsIssue_report = []
                fIssue_report.readline()        # del Labcenter Memo line
                for line in fIssue_report : 
                        lsIssue_report.append(line.strip())
                        if lsIssue_report[-1] == "" : 
                                del lsIssue_report[-1]
                fIssue_report.close()
                if lsIssue_report == [] :
                        return lsSample_data
        #print(lsIssue_report)
        lsIssue_sex = []
        sMapped_yield = ""
        for i in range(0, len(lsIssue_report)) : 
                if "Labcenter-Analysis(LC,A)" in lsIssue_report[i] : 
                        #print(lsIssue_report[i])
                        lsIssue_sex = lsIssue_report[i].split("Labcenter-Analysis(LC,A) : ")[1].split(" ")
                        for k in range(0, len(lsIssue_sex)) : 
                                if lsIssue_sex[k] == "F" : 
                                        lsIssue_sex[k] = "여"
                                elif lsIssue_sex[k] == "M" : 
                                        lsIssue_sex[k] = "남"
                        print("등록({0}) 분석({1})".format(lsIssue_sex[0], lsIssue_sex[1]))
                if "Mapped yield" in lsIssue_report[i] : 
                        if int(lsIssue_report[i].split("Mapped yield : ")[1]) < 350000000 : 
                                sMapped_yield = lsIssue_report[i].split("Mapped yield : ")[1]
                        print(sMapped_yield)

        for i in range(0, len(lsSample_data)) :
                sSample_tmp = lsSample_data[i][1]
                if lsSample_data[i][7] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][7]
                if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] :
                        sSample_tmp += "2"      # LR2 or SR2
                elif lsSample_data[i][8] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][8]
                if sSample == sSample_tmp : 
                        # write sex error
                        if lsIssue_sex != [] : 
                                if len(lsSample_data[i]) == 15 : 
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("성별 확인 요망 등록({0}) 분석({1}) 렙센터 성별수정 확인".format(lsIssue_sex[0], lsIssue_sex[1]))
                                elif len(lsSample_data[i]) == 16 : 
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("성별 확인 요망 등록({0}) 분석({1}) 렙센터 성별수정 확인".format(lsIssue_sex[0], lsIssue_sex[1]))
                                elif len(lsSample_data[i]) == 17 :
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("성별 확인 요망 등록({0}) 분석({1}) 렙센터 성별수정 확인".format(lsIssue_sex[0], lsIssue_sex[1]))
                                elif len(lsSample_data[i]) == 19 :
                                        lsSample_data[i].append("성별 확인 요망 등록({0}) 분석({1}) 렙센터 성별수정 확인".format(lsIssue_sex[0], lsIssue_sex[1]))
                                elif len(lsSample_data[i]) == 20 :
                                        lsSample_data[i][-1] += ", 성별 확인 요망 등록({0}) 분석({1}) 렙센터 성별수정 확인".format(lsIssue_sex[0], lsIssue_sex[1])
                        # write row Mapped_yield
                        if sMapped_yield != "" : 
                                #"{0:,}".format(int(12345)) -> 12,345
                                if len(lsSample_data[i]) == 15 :
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("Mapped_yield {0}".format( "{0:,}".format(int(sMapped_yield)) ))
                                elif len(lsSample_data[i]) == 16 :
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("Mapped_yield {0}".format( "{0:,}".format(int(sMapped_yield)) ))
                                elif len(lsSample_data[i]) == 17 :
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("Mapped_yield {0}".format( "{0:,}".format(int(sMapped_yield)) ))
                                elif len(lsSample_data[i]) == 19 :
                                        lsSample_data[i].append("Mapped_yield {0}".format( "{0:,}".format(int(sMapped_yield)) ))
                                elif len(lsSample_data[i]) == 20 :
                                        lsSample_data[i][-1] += ", Mapped_yield {0}".format( "{0:,}".format(int(sMapped_yield)) )

        return lsSample_data


def append_chr_ratio_abnormal(lsSample_data, sRun_dir, sSample, lsChr_ratio_abnormal) : 
        sChr_ratio_abnormal = ""
        for i in range(0, len(lsChr_ratio_abnormal)) : 
                if type(lsChr_ratio_abnormal[i][0]) == int : 
                        lsChr_ratio_abnormal[i][0] = lsChr_ratio_abnormal[i][0] + 1
                if lsChr_ratio_abnormal[i][0] == 23 : 
                        lsChr_ratio_abnormal[i][0] = "chrX"
                elif lsChr_ratio_abnormal[i][0] == 24 : 
                        lsChr_ratio_abnormal[i][0] = "chrY"
                else : 
                        lsChr_ratio_abnormal[i][0] = "chr" + str(lsChr_ratio_abnormal[i][0])
                if sChr_ratio_abnormal == "" : 
                        sChr_ratio_abnormal += lsChr_ratio_abnormal[i][0] + " ratio " + lsChr_ratio_abnormal[i][1]
                else : 
                        sChr_ratio_abnormal += ", " + lsChr_ratio_abnormal[i][0] + " ratio " + lsChr_ratio_abnormal[i][1]
                
        sSample_dir = sRun_dir + sSample + "/"
        for i in range(0, len(lsSample_data)) : 
                sSample_tmp = lsSample_data[i][1]
                if lsSample_data[i][7] != "NA" : 
                        sSample_tmp += "-" + lsSample_data[i][7]
                if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] :
                        sSample_tmp += "2"      # LR2 or SR2
                elif lsSample_data[i][8] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][8]
                if sSample == sSample_tmp and sChr_ratio_abnormal != "" : 
                        if len(lsSample_data[i]) == 15 : 
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                lsSample_data[i].append("{0}".format(sChr_ratio_abnormal))
                        elif len(lsSample_data[i]) == 16 : 
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                lsSample_data[i].append("{0}".format(sChr_ratio_abnormal))
                        elif len(lsSample_data[i]) == 17 :
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                lsSample_data[i].append("{0}".format(sChr_ratio_abnormal))
                        elif len(lsSample_data[i]) == 20 :
                                lsSample_data[i][-1] += ", {0}".format(sChr_ratio_abnormal)
                        print("chr ratio {0}".format(sChr_ratio_abnormal))

        return lsSample_data


def append_clinvar(lsSample_data, sRun_dir, sSample) : 
        sSample_dir = sRun_dir + sSample + "/"
        for i in range(0, len(lsSample_data)) : 
                sSample_tmp = lsSample_data[i][1]
                if lsSample_data[i][7] != "NA" : 
                        sSample_tmp += "-" + lsSample_data[i][7]
                if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] :
                        sSample_tmp += "2"      # LR2 or SR2
                elif lsSample_data[i][8] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][8]
                if sSample == sSample_tmp : 
                        if sSample + "_decision_call.result" in os.listdir(sSample_dir) : 
                                # decision_call.result : ['chrNum', 'start', 'end', 'range', 'avgRatio', 'No.spot', 'Red.spot', 'Orange.spot', 'Black.spot', 'Disease.name', 'd_chrNum', 'd_start', 'd_end', 'd_range', 'd_No.spot', 'd_overlap_No.spot', 'd_overlap_Red.spot', 'd_overlap_Orange.spot', 'd_overlap_Black.spot', 'd_overlap_Region.pct', 'Method', 'CytoBand', 'ClinVarCNV', 'DGV', 'DECIPHER_Population']
                                # ['chr3', '66575001', '66925000', '350.00Kb', '1.44', '8', '2', '5', '1', '', '', '', '', '', '', '', '', '', '', '', 'Off-target-CNV', '3p14.1', 'Benign;chr3:65470757-67269091;RCV000140759', '-;chr0:0-0', '0/0;chr0:0-0']
                                fDecision_call_result = open(sSample_dir + sSample + "_decision_call.result", 'r')
                                fDecision_call_result.readline()        # del header
                                sClinvar = ""
                                lsMust_retest = []
                                while True : 
                                        k = fDecision_call_result.readline().strip()
                                        if k != "" : 
                                                k = k.split("\t")
                                                sClinvar_tmp = k[22]
                                                sDisease_tmp = k[9]
                                                #print(sClinvar_tmp.split(";")[0])
                                                if "Pathogenic" in sClinvar_tmp :
                                                        if sClinvar == "" : 
                                                                sClinvar = k[0] + ":" + '{0:,}'.format(int(k[1])) + "-" + '{0:,}'.format(int(k[2])) + " " + k[3] + " CNV " + k[4] + " " + " " + sClinvar_tmp.split(";")[0]
                                                        else : 
                                                                #sClinvar = sClinvar + ", " + " ".join(k[:6]) + " " + k[0] + " " + '{0:,}'.format(int(k[1])) + " " + '{0:,}'.format(int(k[2])) + " " + " ".join(k[3:6]) + " " + sClinvar_tmp.split(";")[0]
                                                                sClinvar = sClinvar + ", " + k[0] + ":" + '{0:,}'.format(int(k[1])) + "-" + '{0:,}'.format(int(k[2])) + " " + k[3] + " CNV " + k[4] + " " + " " + sClinvar_tmp.split(";")[0]

                                                if "DiGeorge_syndrome" == sDisease_tmp : 
                                                        lsMust_retest.append(sDisease_tmp)
                                                #######################################################################
                                                # append decision_call to lsSample_data if size is above 1Mb
                                                if k[3] == "1000.00Kb" or "Mb" in k[3] : 
                                                        sWrite_tmp = "{0}:{1}-{2} CNV {3} {4}".format(k[0], '{0:,}'.format(int(k[1])), '{0:,}'.format(int(k[2])), k[4], k[3])
                                                        if len(lsSample_data[i]) == 15 :
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("{0}".format(sWrite_tmp))
                                                        elif len(lsSample_data[i]) == 16 :
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("{0}".format(sWrite_tmp))
                                                        elif len(lsSample_data[i]) == 17 :
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("{0}".format(sWrite_tmp))
                                                        elif len(lsSample_data[i]) == 18 :
                                                                lsSample_data[i].append("")
                                                                lsSample_data[i].append("{0}".format(sWrite_tmp))
                                                        elif len(lsSample_data[i]) == 19 :
                                                                lsSample_data[i].append("{0}".format(sWrite_tmp))
                                                        elif len(lsSample_data[i]) == 20 :
                                                                lsSample_data[i][-1] += ", {0}".format(sWrite_tmp)
                                                # end : append decision_call to lsSample_data if size is above 1Mb
                                                #######################################################################

                                        else : 
                                                break
                                #print("asdfasdf", sClinvar)

                                #########################################################################
                                # append clinvar
                                if sClinvar != "" : 
                                        if len(lsSample_data[i]) == 15 : 
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("{0}".format(sClinvar.split(";")[0]))
                                        elif len(lsSample_data[i]) == 16 :
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("{0}".format(sClinvar.split(";")[0]))
                                        elif len(lsSample_data[i]) == 17 :
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("{0}".format(sClinvar.split(";")[0]))
                                        elif len(lsSample_data[i]) == 19 :
                                                lsSample_data[i][18] = lsSample_data[i][18] + ", {0}".format(sClinvar)
                                        elif len(lsSample_data[i]) == 20 :
                                                lsSample_data[i][18] = "{0}".format(sClinvar.split(";")[0])
                                        #else : 
                                        #        lsSample_data[i][18] = lsSample_data[i][18] + ", {0}".format(sClinvar)
                                        print("ClinVar {0}".format(sClinvar))
                                        
                                ##########################################################################
                                # must re-test list
                                # digeorge (200921 - woo said)
                                if lsMust_retest != [] : 
                                        if len(lsSample_data[i]) == 15 :
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("재검 질병 call : {0}".format(", ".join(lsMust_retest)))
                                        elif len(lsSample_data[i]) == 16 :
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("재검 질병 call : {0}".format(", ".join(lsMust_retest)))
                                        elif len(lsSample_data[i]) == 17 :
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("")
                                                lsSample_data[i].append("재검 질병 call : {0}".format(", ".join(lsMust_retest)))
                                        elif len(lsSample_data[i]) == 19 :
                                                lsSample_data[i].append("재검 질병 call : {0}".format(", ".join(lsMust_retest)))
                                        elif len(lsSample_data[i]) == 20 :
                                                lsSample_data[i][19] += ", 재검 질병 call : {0}".format(", ".join(lsMust_retest))
                                        print("재검 질병 call :  {0}".format(", ".join(lsMust_retest)))         
                                ##########################################################################
                                fDecision_call_result.close()
                        else : 
                                print("Don't exist {0}_decision_call.result".format(sSample))
        
        return lsSample_data


#def append_mapped_read(lsSample_data, sRun_dir, sSample) : 
#        sSample_dir = sRun_dir + sSample + "/"
#        for i in range(0, len(lsSample_data)) : 
#                sSample_tmp = lsSample_data[i][1]
#                if lsSample_data[i][7] != "NA" : 
#                        sSample_tmp += "-" + lsSample_data[i][7]
#                if lsSample_data[i][8] != "NA" : 
#                        sSample_tmp += "-" + lsSample_data[i][8]
#                if sSample == sSample_tmp : 
#                        if sSample + ".uniq.reads.count" in os.listdir(sSample_dir + sSample + "/") :



def write_sample_data_result(lsSample_data) : 

        fSample_data_result_test = open("/home/shinejh0528/sample_data_result.txt", 'w')
        for i in range(0, len(lsSample_data)) :
                print("=".join(lsSample_data[i]))
                fSample_data_result_test.write("=".join(lsSample_data[i]) + "\n")
        fSample_data_result_test.close()


def turn_date(sSample, lsSample_data) : 
        id = sSample[:13]
        js_url = "http://labge02:8080/enfantguard/api/enfantguard/%s/%s?key=%s" %(id,sSample,key)
        data = urllib.urlopen(js_url).read()
        try :
                js_data = json.loads(data)
        except :
                print("{0} is not a sample or don't sexist in DB".format(sample))
        lsKey_js_data = list(js_data.keys())

        sSystem_date = str(js_data["sample"]["turnDate"])[:10]
        #print(u'{0}'.format( str(js_data["sample"]["sampleName"]) ))
        #print(js_data["sample"]["sampleName"])
        sSample_type = js_data["sample"]["sampleName"]
        print(sSample_type)
        try : 
                sTurnDate = str(datetime.datetime.fromtimestamp(int(sSystem_date)).strftime('%Y%m%d %H:%M:%S')).split(" ")[0]
        except : 
                print("turn_date None type error")
                return
        #print(Datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        sCurrent_time = str(Datetime.today().strftime("%Y%m%d %H:%M:%S")).split(" ")[0]
        #print(sTurnDate)
        if int(sTurnDate) <= int(sCurrent_time) : 
                print(sTurnDate)
                for i in range(0, len(lsSample_data)) : 
                        sSample_tmp = lsSample_data[i][1]
                        if lsSample_data[i][7] != "NA" : 
                                sSample_tmp += "-" + lsSample_data[i][7]
                        if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] :
                                sSample_tmp += "2"      # LR2 or SR2
                        elif lsSample_data[i][8] != "NA" :
                                sSample_tmp += "-" + lsSample_data[i][8]
                        if sSample == sSample_tmp : 
                                if len(lsSample_data[i]) == 15 : 
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("TAT날짜 {0}".format(sTurnDate))
                                elif len(lsSample_data[i]) == 16 :
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("TAT날짜 {0}".format(sTurnDate))
                                elif len(lsSample_data[i]) == 17 :
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("TAT날짜 {0}".format(sTurnDate))
                                elif len(lsSample_data[i]) == 19 :
                                        lsSample_data[i].append("TAT날짜 {0}".format(sTurnDate))
                                elif len(lsSample_data[i]) == 20 :
                                        lsSample_data[i][19] += ", TAT날짜 {0}".format(sTurnDate)
        lsTest = []
        for i in range(0, len(lsSample_data)) :
                sSample_tmp = lsSample_data[i][1]
                if lsSample_data[i][7] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][7]
                if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] :
                        sSample_tmp += "2"      # LR2 or SR2
                elif lsSample_data[i][8] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][8]
                if sSample == sSample_tmp :
                        if len(lsSample_data[i]) >= 20 : 
                                if "chrX" in lsSample_data[i][19] or "chrY" in lsSample_data[i][19] : 
                                        print(type(sSample_type))
                                        lsTest.append(sSample_type)
                                        try : 
                                                lsSample_data[i][19] += ", 검체 종류 {0}".format(sSample_type)
                                        except : 
                                                lsSample_data[i][19] += ", 검체 종류 unicode error"
        return lsSample_data


def read_micro_disease_info() : 
        # ['chrX', '147100001', '155000000', 'Xq28_duplication_syndrome', 'gain', '1.25', '2.25', '1', '1', 'Xq28 \xec\xa4\x91\xeb\xb3\xb5 \xec\xa6\x9d\xed\x9b\x84\xea\xb5\xb0', '(Xq28 duplication syndrome)']
        # [0] chr [1] start [2] end [3] disease with underbar [4] 'gain' or 'loss' 
        sMicro_disease_info_file = "/home/shinejh0528/EnfantGuard_micro_disease.ver3.info"
        fMicro_disease_info = open(sMicro_disease_info_file, 'r')
        lsMicro_disease_info = []
        
        for i in fMicro_disease_info : 
                lsMicro_disease_info.append(i.strip().split("\t"))

        fMicro_disease_info.close()

        return lsMicro_disease_info


def read_RefSeq() : 
        # ['chrY', '2803421', '2850547', 'ZFY']
        # [0] chr [1] start [2] end [3] gene
        sRefSeq_file = "/home/shinejh0528/RefSeq_genes_all_full_length_201120.bed"
        fRefSeq = open(sRefSeq_file, 'r')
        lsRefSeq = []

        for i in fRefSeq : 
                lsRefSeq.append(i.strip().split("\t"))

        fRefSeq.close()

        return lsRefSeq


def call_MicDis_gene_in_decision(lsSample_data, sRun_dir, sSample, lsMicDis_info, lsRefSeq, fMicDis_gene_in_decision) : 
        sSample_dir = sRun_dir + sSample + "/"
        lsMicrodisease_decision = []

        for i in range(0, len(lsSample_data)) :
                sSample_tmp = lsSample_data[i][1]
                if lsSample_data[i][7] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][7]
                if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] :
                        sSample_tmp += "2"      # LR2 or SR2
                elif lsSample_data[i][8] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][8]
                if sSample == sSample_tmp :
                        if sSample + "_decision_call.result" in os.listdir(sSample_dir) :
                                fDecision_call_result = open(sSample_dir + sSample + "_decision_call.result", 'r')
                                fDecision_call_result.readline()
                                while True :
                                        k = fDecision_call_result.readline().strip()
                                        if k != "" :
                                                ##################################################################################
                                                # seach gene in microdisease if decision call in microdisease
                                                # step 1 : append decision call in microdisease (-> step2 : search gene)
                                                k = k.split("\t")
                                                for j in range(0, len(lsMicDis_info)) :
                                                        if k[0] != lsMicDis_info[j][0] :
                                                                continue
                                                        #print(k[0], lsMicDis_info[j][0])
                                                        if float(k[4]) > 1 and lsMicDis_info[j][4] == "loss" :
                                                                continue
                                                        if float(k[4]) < 1 and lsMicDis_info[j][4] == "gain" :
                                                                continue
                                                        if ( int(k[1]) <= int(lsMicDis_info[j][1]) and int(k[2]) >= int(lsMicDis_info[j][1]) ) or (int(k[1]) >= int(lsMicDis_info[j][1]) and int(k[1]) <= int(lsMicDis_info[j][2]) ) :
                                                                print(k[1], k[2], lsMicDis_info[j][1], lsMicDis_info[j][2])
                                                                # [0] run_id [1] sample [2] initial [3] chr [4] Decision_start [5] Decision_end [6] CNV [7] range [8] disease_name_with_underbar
                                                                lsMicrodisease_decision.append( [ sRun_dir.split("/")[-2], sSample, lsSample_data[i][9], k[0], k[1], k[2], k[4], k[3], lsMicDis_info[j][3] ])
                                                                #print(lsMicrodisease_decision[-1])
                                                                # '{0:,}'.format(int(k[1]))
                                                ##################################################################################
                                        else :
                                                break
                                fDecision_call_result.close()
                        
                        ############################################################################
                        # seach gene in microdisease if decision call in microdisease
                        # step 2 : if decision_call in microdisease, seach gene in microdisease ( step 1 : append decision call in microdisease )
                        if lsMicrodisease_decision == [] :
                                #print("lsMicrodisease_decision == []")
                                return
                        for j in range(0, len(lsMicrodisease_decision)) :
                                for k in range(0, len(lsRefSeq)) :
                                        # [0] chr [1] start [2] end [3] gene
                                        if lsRefSeq[k][0] != lsMicrodisease_decision[j][3] :
                                                continue
                                        if ( int(lsRefSeq[k][1]) >= int(lsMicrodisease_decision[j][4]) and int(lsRefSeq[k][1]) <= int(lsMicrodisease_decision[j][5]) ) or ( int(lsRefSeq[k][2]) >= int(lsMicrodisease_decision[j][4]) and int(lsRefSeq[k][2]) <= int(lsMicrodisease_decision[j][5]) ) or ( int(lsRefSeq[k][1]) <= int(lsMicrodisease_decision[j][4]) and int(lsRefSeq[k][2]) >= int(lsMicrodisease_decision[j][5]) ) :
                                                # [0] run_id [1] sample [2] initial [3] chr [4] Decision_start [5] Decision_end [6] CNV [7] range [8] disease_name_with_underbar [9] RefSeq_gene [10] RefSeq_gene_S [11] RefSeq_gene_E
                                                print("MicDis_gene_in_decision : {0}\t{1}".format(" ".join(lsRefSeq[k]), " ".join(lsMicrodisease_decision[j]) ))
                                                if len(lsMicrodisease_decision[j]) == 9 : 
                                                        lsMicrodisease_decision[j].append(lsRefSeq[k][3])
                                                else : 
                                                        lsMicrodisease_decision[j][9] += ", {0}".format(lsRefSeq[k][3])
                                                #print(lsMicrodisease_decision[j])
                        ############################################################################
        # for i loop end
        #######################################################################
        for i in range(0, len(lsMicrodisease_decision)) : 
                fMicDis_gene_in_decision.write("\t".join(lsMicrodisease_decision[i][:3]) + "\t" + lsMicrodisease_decision[i][3] + ":" + '{0:,}'.format(int(lsMicrodisease_decision[i][4])) + "-" + '{0:,}'.format(int(lsMicrodisease_decision[i][5])) + "\t" + "\t".join(lsMicrodisease_decision[i][6:]) + "\n")



def write_peri_MicDis_in_lsSample_data(lsSample_data, sRun_dir, sSample, lsPeri_MicDis_CNV) : 
        # lsPeri_MicDis_CNV[i][0] seg_chr, [1] seg_S [2] seg_E [3] CNV [4] range [5] sBase_unit (Kb or Mb) [6] disease_with_under_bar
        # append Peri_MicDis_CNV to lsSample_data[i][21]
        for i in range(0, len(lsSample_data)) :
                sSample_tmp = lsSample_data[i][1]
                if lsSample_data[i][7] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][7]
                if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] : 
                        sSample_tmp += "2"      # LR2 or SR2
                elif lsSample_data[i][8] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][8]
                if sSample == sSample_tmp : 
                        for j in range(0, len(lsPeri_MicDis_CNV)) :
                                # append to lsSample_data[i][21]
                                # '{0:,}'.format(int(lsSepa_seg[i][2]))
                                # "{0:,}".format(int(lsPeri_MicDis_CNV[j][1])), "{0,:}".format(int(lsPeri_MicDis_CNV[j][2]))
                                if len(lsSample_data[i]) == 15 :
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")     # [20]
                                        lsSample_data[i].append("{0}:{1}-{2} CNV {3} {4}{5} {6} 주변".format(lsPeri_MicDis_CNV[j][0], "{0:,}".format(int(lsPeri_MicDis_CNV[j][1])), "{0:,}".format(int(lsPeri_MicDis_CNV[j][2])), lsPeri_MicDis_CNV[j][3], lsPeri_MicDis_CNV[j][4], lsPeri_MicDis_CNV[j][5], lsPeri_MicDis_CNV[j][6]))       # [21]
                                elif len(lsSample_data[i]) == 16 : 
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")     # [20]
                                        lsSample_data[i].append("{0}:{1}-{2} CNV {3} {4}{5} {6} 주변".format(lsPeri_MicDis_CNV[j][0], "{0:,}".format(int(lsPeri_MicDis_CNV[j][1])), "{0:,}".format(int(lsPeri_MicDis_CNV[j][2])), lsPeri_MicDis_CNV[j][3], lsPeri_MicDis_CNV[j][4], lsPeri_MicDis_CNV[j][5], lsPeri_MicDis_CNV[j][6]))       # [21]
                                elif len(lsSample_data[i]) == 17 :
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")     # [20]
                                        lsSample_data[i].append("{0}:{1}-{2} CNV {3} {4}{5} {6} 주변".format(lsPeri_MicDis_CNV[j][0], "{0:,}".format(int(lsPeri_MicDis_CNV[j][1])), "{0:,}".format(int(lsPeri_MicDis_CNV[j][2])), lsPeri_MicDis_CNV[j][3], lsPeri_MicDis_CNV[j][4], lsPeri_MicDis_CNV[j][5], lsPeri_MicDis_CNV[j][6]))       # [21]
                                elif len(lsSample_data[i]) == 18 :
                                        lsSample_data[i].append("")
                                        lsSample_data[i].append("")     # [20]
                                        lsSample_data[i].append("{0}:{1}-{2} CNV {3} {4}{5} {6} 주변".format(lsPeri_MicDis_CNV[j][0], "{0:,}".format(int(lsPeri_MicDis_CNV[j][1])), "{0:,}".format(int(lsPeri_MicDis_CNV[j][2])), lsPeri_MicDis_CNV[j][3], lsPeri_MicDis_CNV[j][4], lsPeri_MicDis_CNV[j][5], lsPeri_MicDis_CNV[j][6]))       # [21]
                                elif len(lsSample_data[i]) == 19 :
                                        lsSample_data[i].append("")     # [20]
                                        lsSample_data[i].append("{0}:{1}-{2} CNV {3} {4}{5} {6} 주변".format(lsPeri_MicDis_CNV[j][0], "{0:,}".format(int(lsPeri_MicDis_CNV[j][1])), "{0:,}".format(int(lsPeri_MicDis_CNV[j][2])), lsPeri_MicDis_CNV[j][3], lsPeri_MicDis_CNV[j][4], lsPeri_MicDis_CNV[j][5], lsPeri_MicDis_CNV[j][6]))       # [21]
                                elif len(lsSample_data[i]) == 20 :
                                        lsSample_data[i].append("{0}:{1}-{2} CNV {3} {4}{5} {6} 주변".format(lsPeri_MicDis_CNV[j][0], "{0:,}".format(int(lsPeri_MicDis_CNV[j][1])), "{0:,}".format(int(lsPeri_MicDis_CNV[j][2])), lsPeri_MicDis_CNV[j][3], lsPeri_MicDis_CNV[j][4], lsPeri_MicDis_CNV[j][5], lsPeri_MicDis_CNV[j][6]))       # [21]
                                elif len(lsSample_data[i]) == 21 : 
                                        lsSample_data[i][-1] += ", {0}:{1}-{2} CNV {3} {4}{5} {6} 주변".format(lsPeri_MicDis_CNV[j][0], "{0:,}".format(int(lsPeri_MicDis_CNV[j][1])), "{0:,}".format(int(lsPeri_MicDis_CNV[j][2])), lsPeri_MicDis_CNV[j][3], lsPeri_MicDis_CNV[j][4], lsPeri_MicDis_CNV[j][5], lsPeri_MicDis_CNV[j][6])       # [21]
        
        return lsSample_data


def write_MAD_GC_fail_in_lsSample_data(lsSample_data, sRun_dir, sSample, sGC_ratio, sOfftarget_MAD) : 
        for i in range(0, len(lsSample_data)) : 
                sSample_tmp = lsSample_data[i][1]
                if lsSample_data[i][7] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][7]
                if lsSample_data[i][8] != "NA" and lsSample_data[i][8] == lsSample_data[i][7] :
                        sSample_tmp += "2"      # LR2 or SR2
                elif lsSample_data[i][8] != "NA" :
                        sSample_tmp += "-" + lsSample_data[i][8]
                if sSample == sSample_tmp : 
                        if len(lsSample_data[i]) == 15 :
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                if sOfftarget_MAD != "" and sGC_ratio != "" : 
                                        lsSample_data[i][15] = "QC fail(MAD {0}, GC {1})".format(sOfftarget_MAD, sGC_ratio)
                                        lsSample_data[i].append("MAD {0}, GC {1}".format(sOfftarget_MAD, sGC_ratio))
                                elif sOfftarget_MAD != "" and sGC_ratio == "" : 
                                        lsSample_data[i][15] = "QC fail(MAD {0})".format(sOfftarget_MAD)
                                        lsSample_data[i].append("MAD {0}".format(sOfftarget_MAD))
                                elif sOfftarget_MAD == "" and sGC_ratio != "" :
                                        lsSample_data[i][15] = "QC fail(GC {0})".format(sGC_ratio)
                                        lsSample_data[i].append("GC {0}".format(sGC_ratio))
                        elif len(lsSample_data[i]) == 16 : 
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                if sOfftarget_MAD != "" and sGC_ratio != "" :
                                        lsSample_data[i].append("MAD {0}, GC {1}".format(sOfftarget_MAD, sGC_ratio))
                                elif sOfftarget_MAD != "" and sGC_ratio == "" :
                                        lsSample_data[i].append("MAD {0}".format(sOfftarget_MAD))
                                elif sOfftarget_MAD == "" and sGC_ratio != "" :
                                        lsSample_data[i].append("GC {0}".format(sGC_ratio))
                        elif len(lsSample_data[i]) == 17 : 
                                lsSample_data[i].append("")
                                lsSample_data[i].append("")
                                if sOfftarget_MAD != "" and sGC_ratio != "" :
                                        lsSample_data[i].append("MAD {0}, GC {1}".format(sOfftarget_MAD, sGC_ratio))
                                elif sOfftarget_MAD != "" and sGC_ratio == "" :
                                        lsSample_data[i].append("MAD {0}".format(sOfftarget_MAD))
                                elif sOfftarget_MAD == "" and sGC_ratio != "" :
                                        lsSample_data[i].append("GC {0}".format(sGC_ratio))
                        elif len(lsSample_data[i]) == 18 : 
                                lsSample_data[i].append("")
                                if sOfftarget_MAD != "" and sGC_ratio != "" :
                                        lsSample_data[i].append("MAD {0}, GC {1}".format(sOfftarget_MAD, sGC_ratio))
                                elif sOfftarget_MAD != "" and sGC_ratio == "" :
                                        lsSample_data[i].append("MAD {0}".format(sOfftarget_MAD))
                                elif sOfftarget_MAD == "" and sGC_ratio != "" :
                                        lsSample_data[i].append("GC {0}".format(sGC_ratio))
                        elif len(lsSample_data[i]) == 19 : 
                                if sOfftarget_MAD != "" and sGC_ratio != "" :
                                        lsSample_data[i].append("MAD {0}, GC {1}".format(sOfftarget_MAD, sGC_ratio))
                                elif sOfftarget_MAD != "" and sGC_ratio == "" :
                                        lsSample_data[i].append("MAD {0}".format(sOfftarget_MAD))
                                elif sOfftarget_MAD == "" and sGC_ratio != "" :
                                        lsSample_data[i].append("GC {0}".format(sGC_ratio))
                        elif len(lsSample_data[i]) == 20 : 
                                if sOfftarget_MAD != "" and sGC_ratio != "" :
                                        lsSample_data[i] += ", MAD {0}, GC {1}".format(sOfftarget_MAD, sGC_ratio)
                                elif sOfftarget_MAD != "" and sGC_ratio == "" :
                                        lsSample_data[i] += ", MAD {0}".format(sOfftarget_MAD)
                                elif sOfftarget_MAD == "" and sGC_ratio != "" :
                                        lsSample_data[i] += ", GC {0}".format(sGC_ratio)
        # for i loop end

        return lsSample_data




def main() : 
        print("업데이트(200331) : 1. 양성콜도 영역 겹침이나 중요유전자 포함하는지 분석하도록 수정 2. 양성콜이 같은게 2개 이상 나오면 하나만 써지도록 수정 3. 앙팡 분석 파이프라인 적용하여 전체 probe 수 > (seg_size / 50000) * 0.2일 때 disease_call 되도록 수정 4. SR, LR, Merged 분석 후 write 안 되는 것 수정, 5. chr seg_start end 중복으로 써지는 것 안 써지게 수정")
        print("업데이트(200409) : 1. 랩센터와 분석 성별이 일치하지 않을 때 issue call")
        print("업데이트(200417) : 1. separated_seg 가 chrY 일 때, seg weight 0.2 -> 0.1 이 되도록 수정  2.  segment size (Kb, Mb) 출력되도록 추가")
        print("업데이트(200508) : 자잘한 오류 수정 및 issue 출력 방식 수정, chr15 segment 분석 안 되는 것 수정, 2. 15q26_overgrowth_syndrome - (IGF1R) 유전자 추가")
        print("업데이트(200511) : 1. chr ratio 1.03 이상이면 report 2. ClinVar Pathogenic이면 report")
        print("업데이트(200512) : 1. no seg size cutoff, 2. 1000단위 콤마(,)  구분 ")
        print("업데이트(200520) : Idiopathic_generalized_epilepsy - panel gene  유전자 (SLC12A6) 추가")
        print("업데이트(200604) : chr|X-Y| ratio >= 0.05 이면 이슈란 입력 추가")
        print("업데이트(200618) : TAT 가 현재 날짜보다 이전이면 이슈란 입력 추가.")
        print("업데이트(200727) : log ratio cutoff 0.06에서 0.08로 변경")
        print("업데이트(200728) : 8p23.1 duplication syndrome 유전자 MFHAS1, MSRA 삭제(panel gene)")
        print("업데이트(200903) : 1p32-p31_deletion_syndrome NFIA panel gene 추가, 200902  메세지 참조")
        print("업데이트(200907) : 17p13.3_Centromeric_duplication_syndrome (PAFAH1B1), (YWHAE) 검사 유전자 추가")
        print("업데이트(200911) : 5 Mb 이하 작은 사이즈 질병이면 issue에 질병 사이즈 write, 작은 사이즈 질병은 음성 판정 가능일지라도 사이즈 확인 필요(우경주임님)")
        print("업데이트(200921) : append_clinvar(lsSample_data, sRun_dir, sSample) 함수에 재검 질병 call 기능 추가(우경주임님, call 되면 must re-test) : Digeorge_syndrome, Digeorge 유전자 CRKL 추가")
        print("업데이트(201005) : 2p12-p11.2_deletion_syndrome panel gene REEP1 추가. '9월 28일 김과장님 REEP1 결실에 대한 보고가 있어 리뷰라도 보고싶다'고 언급한 gene + CTNNA2 gene 추가. 우경주임님 해당 질병의 주요유전자로 보여지는 연구가 있다고 자료 제시. LRRTM1 은 CTNNA2 gene 영역 안에 있어 추가 불필요.")
        print("업데이트(201007) : segment size 가 Kb 단위일 경우 소수점 삭제( ex) 400.00 Kb -> 400 Kb )")
        print("업데이트(201015) : Deafness_Dystonia_and_Cerebral_hyomyelination의 panel gene 유전자 IDS 추가. 201015 김과장님 IDS gene이 포함으로  재검 의견.")
        print("업데이트(201104) : append_disease_call_in_lsSample_data(lsSample_data, sRun_dir, sSample) 함수 양성 콜 2개 이상인데 1개만 써지는 오류 수정")
        print("임시업데이트(201113) : 분리된 segment가 ISCA gene 포함시/home/shinejh0528/separated_seg_analyis/seg_include_ISCA/[run_id]_seg_include_ISCA.txt 생성. 추후 사용 용이하게 업데이트 필요.")
        print("업데이트(201113) : ISCA 기능 지속 업데이트중, (201117) : initial 추가")
        print("업데이트(201119) : microdeletion 있을 때 decision call에 포함된 gene있으면 call해주는 기능 추가, (201124) : 추가 업데이트. 파일 생성. call_MicDis_gene_in_decision(lsSample_data, sRun_dir, sSample, lsMicDis_info, lsRefSeq, fMicDis_gene_in_decision) function 추가")
        # ISCA.bed  업데이트 : chrY 14542921    15094080    AZFa 없음 -> 지우고 해당 영역에 포함된 chrY   14774297    14804153    TTTY15, chrY    14813159    14972764    USP9Y, chrY 15015909    15032390    DDX3Y으로 대체
        print("업데이트(201127) : append_clinvar(lsSample_data, sRun_dir, sSample)에 decision_call이 1 Mb 이상이면 lsSample_data[20]에 append 기능 추가, ISCA call : segment가 dup인지 del인지 명시 추가")
        print("업데이트(201202) : 22q11.2_distal_deletion_syndrome 유전자 MAPK1, SMARCB1 추가. rarechromo에서 언급됨")
        print("업데이트(201205) : Peri_microdisease CNV 검색 기능 추가. SR2, LR2 데이터 매칭 실패하는 것 수정") # 201203_NB501509_0739_AHL2KNAFX2 처럼 LR2가 있는 경우lsSample_data에 정보를 추가하지 못한다. 분석은 서버 폴더명을 가져오는 거라 상관 없고 lsSample_data와 매칭할 때 에러가 난다. SR2, LR2의 경우만 lsSample[i][7], [8]에 LR이  같이 써지며 그 이상이면 [7]에만 LR3, LR4와 같이 적힌다.")
        print("업데이트(201215) : 17p13.3_Cemtromeric_duplication_syndrome VPS53 gene 추가")
        print("업데이트(210114) : 22q11.2_distal_deletion_syndrome SMARCB1 삭제. 질환을 가진 대부분이 이 gene을 포함하지 않는다는, 암 관련 유전자라는 내용.")
        print("업데이트(210127) : 기존 seg_analysis를 제외한 segment가 microdisease 내에 있으면 issue에 추가하는 call MicDis 기능 추가")
        print("업데이트(210121) : MAD, GC QC fail일 때 write 함수 작성 기능 추가")
        
        sGC_ratio = ""
        sOfftarget_MAD = ""
        boolPass = True

        optlist = option()
        if optlist == [] : 
                sys.exit()
        
        if "sample_data_result.txt" in os.listdir("/home/shinejh0528/") : 
                os.system("rm /home/shinejh0528/sample_data_result.txt")

        sEnfantGuard_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/"
        sSeg_include_ISCA_dir = "/home/shinejh0528/separated_seg_analyis/seg_include_ISCA/"
        sMicDis_gene_in_decision_file_dir = "/home/shinejh0528/separated_seg_analyis/gene_microdisease_in_decision/"

        sRun_ID = optlist[0][1]
        sRun_dir = sEnfantGuard_dir + sRun_ID + "/"
        lsSample_data = samplesheet_py(sRun_ID)
        print("")

        fSeparated_seg = open("/home/shinejh0528/separated_seg_analyis/{0}_separated_seg.txt".format(sRun_ID), 'w')
        fMicDis_gene_in_decision = open(sMicDis_gene_in_decision_file_dir + "{0}_microdisease_gene_in_decision.txt".format(sRun_ID), 'w')
        #fSeg_disease_call = open("/data/Tools/bin/separated_seg_analyis/{0}_separated_seg_disease_call.txt".format(sRun_ID), 'w')
        fSeg_include_ISCA = open("{0}{1}_seg_include_ISCA.txt".format(sSeg_include_ISCA_dir, sRun_ID), 'w')
        fSeg_include_ISCA.write("run_id\tsample\tinitial\tsegment\tCNV\tsize\tDupOrDel\tISCA_gene\n")
        
        lsChr_ratio_abnormal = []
        lsDisease_genes = read_disease_genes()
        lsISCA = read_ISCA_bed()
        lsPanel_gene = read_panel_gene_bed()
        lsMicro_disease_info = read_micro_disease_info()
        lsRefSeq = read_RefSeq()
        lsPeri_MicDis_CNV = []
        
        nCount_sample = 1
        for sSample in os.listdir(sRun_dir) : 
                print("{0}\tSample_ID : {1}".format(str(nCount_sample), sSample))
                nCount_sample += 1
                boolPass, lsChr_ratio_abnormal, sGC_ratio, sOfftarget_MAD = quality_check(sRun_dir, sSample)
                if boolPass == False : 
                        print("{0} don't pass quality or file check".format(sSample))
                        lsSample_data = write_MAD_GC_fail_in_lsSample_data(lsSample_data, sRun_dir, sSample, sGC_ratio, sOfftarget_MAD)
                        boolPass == True
                        #continue
                boolPass, lsSepa_seg = extract_seg(sRun_dir, sSample, fSeparated_seg)
                #print("check 7", type(lsSample_data))       ########### none type beginning
                if boolPass == False :
                        print("{0} don't has {1}_segment.output.txt".format(sSample, sSample))
                        boolPass = True
                        continue
                lsSample_data = append_disease_call_in_lsSample_data(lsSample_data, sRun_dir, sSample)
                lsSample_data, lsPeri_MicDis_CNV = separated_seg_analysis(sRun_dir, sSample, lsDisease_genes, lsSepa_seg, lsSample_data, lsISCA, lsPanel_gene, fSeg_include_ISCA, lsMicro_disease_info)
                lsSample_data = append_negative_in_lsSample_data(lsSample_data,sRun_dir, sSample)
                issue_call(lsSample_data, sRun_dir, sSample)
                lsSample_data = append_clinvar(lsSample_data, sRun_dir, sSample)
                lsSample_data = append_chr_ratio_abnormal(lsSample_data, sRun_dir, sSample, lsChr_ratio_abnormal)
                lsSample_date = turn_date(sSample, lsSample_data)
                call_MicDis_gene_in_decision(lsSample_data, sRun_dir, sSample, lsMicro_disease_info, lsRefSeq, fMicDis_gene_in_decision)
                lsSample_data = write_peri_MicDis_in_lsSample_data(lsSample_data, sRun_dir, sSample, lsPeri_MicDis_CNV)
                print("\n\n")
        time.sleep(1)
        print("\n\n")
        write_sample_data_result(lsSample_data)
        #for i in range(0, len(lsSample_data)) : 
        #        print(lsSample_data[i])
        
        fSeparated_seg.close()
        #fSeg_disease_call.close()
        fSeg_include_ISCA.close()
        fMicDis_gene_in_decision.close()

main()
