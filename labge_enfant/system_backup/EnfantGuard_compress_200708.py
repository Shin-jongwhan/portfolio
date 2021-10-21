#!/usr/bin/python
# -*- coding:utf-8 -*-

#os.system("python /home/shinejh0528/samplesheet_jh.py {0}".format(sRun_ID))

import sys
import os

sCommend = sys.argv[1]
sRun_id = sys.argv[2]
sSample = sys.argv[3]

sAnalysis_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data"

#print("Commend : {0}".format(sCommend))
print("Run_id {0} Sample {1}".format(sRun_id, sSample))


def Compress(sRun_id, sSample) : 
    os.system("tar -zcvf {0}@{1}.tar.gz {2}/{3]/{4}/*".format(sSample, sRun_id, sAnalysis_dir, sRun_id, sSample))


def main() : 
        if sCommend == "Compress" : 
                Compress(sRun_id, sSample)
