#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys, glob
import os

Analysis_dir = "/data/kws1013/Demultiplexing/"
Run_dir = sys.argv[1]
out_file = file(Analysis_dir + Run_dir + '_Stats_cluster_PM_data.txt', 'w')

sample_dict = {}
dicSample_cluster = {}
indexs = 0 
fastq_file = file(Run_dir + "/Stats/DemultiplexingStats.xml")

boolBarcode = False
for fdata in fastq_file:
	Fdata = fdata.strip()
	if Fdata.split('=')[0] == '<Sample name':
		sample_name = Fdata.split('=')[1][1:-2]
		if sample_name[0:2] == 'Un' : pass
		else:
			sample_dict.setdefault(sample_name, 0)
			dicSample_cluster.setdefault(sample_name, 0)
			indexs = 1
	elif len(Fdata.split('PerfectBarcodeCount')) > 1 : 
		if indexs >= 5 or indexs == 0 : pass
		else:
			sample_dict[sample_name] += int(Fdata.split('PerfectBarcodeCount>')[1].split('</')[0])
			#dicSample_cluster[sample_name] = += int(Fdata.split('BarcodeCount>')[1].split('</')[0])
			indexs += 1
	elif len(Fdata.split("<BarcodeCount>")) > 1 : 
		#print(Fdata)
		if indexs >= 5 or indexs == 0 : pass
		else : 
			#print(Fdata)
			dicSample_cluster[sample_name] += int(Fdata.split('<BarcodeCount>')[1].split('</')[0])
	

def PFclusterCount() :
    Run_dir = sys.argv[1]
    #print(os.listdir(Analysis_dir + Run_dir + "/Reports/html"))
    lsReport_dir_list = os.listdir(Analysis_dir + Run_dir + "/Reports/html")
    sLaneBarcode_dir = ""
    for i in range(0, len(lsReport_dir_list)) :
        if os.path.isdir(Analysis_dir + Run_dir + "/Reports/html/" + lsReport_dir_list[i]) == True :
            if os.path.isdir(Analysis_dir + Run_dir + "/Reports/html/" + lsReport_dir_list[i] + "/default/all/all") == True :
                sLaneBarcode_dir = Analysis_dir + Run_dir + "/Reports/html/" + lsReport_dir_list[i] + "/default/all/all/"

    fLaneBarcode = open(sLaneBarcode_dir + "laneBarcode.html", 'r')
    dicLaneBarcode = {}
    while True :
        i = fLaneBarcode.readline().strip()
        if "</html>" != i :
            if "<td>1</td>" == i :
                sSample = fLaneBarcode.readline().split("<td>")[1].split("</td")[0]
                fLaneBarcode.readline()     # del index line
                nPFcluster = int(fLaneBarcode.readline().split("<td>")[1].split("</td")[0].replace(",", ""))
                dicLaneBarcode[sSample] = nPFcluster
                continue
            if "<td>2</td>" == i or "<td>3</td>" == i or "<td>4</td>" == i :
                sSample = fLaneBarcode.readline().split("<td>")[1].split("</td")[0]
                fLaneBarcode.readline()     # del index line
                nPFcluster = int(fLaneBarcode.readline().split("<td>")[1].split("</td")[0].replace(",", ""))
                dicLaneBarcode[sSample] += nPFcluster
        else :
            break

    lsKey_laneBarcode = list(dicLaneBarcode.keys())
    #for i in lsKey_laneBarcode :
    #   print(i, dicLaneBarcode[i])

    fLaneBarcode.close()
    return dicLaneBarcode

out_file.write("sample\tBarcodeCount(cluster)\tPFcluster\tPerfectBarcodeCount(PM)\n")
dicPFcluster = PFclusterCount()
#lsSample_id = list(dicPFcluster.keys())
#print(lsSample_id)
#print(list(sample_dict.keys()))

for sample_key in sample_dict.keys():
    if sample_key == "all" :
        continue
    print(sample_key + '\t' + str(int(dicSample_cluster[sample_key])) + "\t" + str(int(dicPFcluster[sample_key])) + "\t" + str(int(sample_dict[sample_key])))
    out_file.write(sample_key + '\t' + str(int(dicSample_cluster[sample_key])) + "\t" + str(int(dicPFcluster[sample_key])) + "\t" + str(int(sample_dict[sample_key])) + '\n')
