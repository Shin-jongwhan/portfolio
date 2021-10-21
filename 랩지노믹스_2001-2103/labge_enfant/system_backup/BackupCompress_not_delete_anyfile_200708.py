#!/usr/bin/python


import os,sys,time
import shutil

Analysis_dataDIR = "/data/Analysis/Project/EnfantGuard/Analysis_data"

def GenerationCOMP(runid,sample):
	initDIR = os.getcwd()	
	#set home directory
	homeDIR="%s/%s/%s" %(Analysis_dataDIR,runid,sample)

	
	#make directoy for COMP file tmp
	cpDIR="%s/COMPtmp/" %(homeDIR)
	if not os.path.isdir(cpDIR):
		os.mkdir(cpDIR)
	cpResultDIR="%s/COMPtmp/result/" %(homeDIR)
	if not os.path.isdir(cpResultDIR):
		os.mkdir(cpResultDIR)
	
	# copy analysis list
#	CopyList = ["%s/FASTQ/%s_1.fastq.gz"%(homeDIR,sample),"%s/FASTQ/%s_2.fastq.gz"%(homeDIR,sample), "%s/%s/%s.rmdup.HG19.bam"%(homeDIR,sample,sample),"%s/contra/table/%s.CNATable.20rd.20bases.20bins.txt"%(homeDIR,sample),"%s/contra/table/%s.CNATable.20rd.20bases.20bins.txt.CBS_1.txt"%(homeDIR,sample),"%s/CopywriteR/CNAprofiles/segment.data.txt"%homeDIR,"%s/CopywriteR/CNAprofiles/segment.output.txt"%homeDIR,"%s/CopywriteR/CNAprofiles/segment.Rdata"%homeDIR,"%s/baf/%s.snp138_minR20_minMapQ15_minBaseQ20.baf"%(homeDIR,sample) ]

	CopyList = ["%s/FASTQ/%s_1.fastq.gz"%(homeDIR,sample),"%s/FASTQ/%s_2.fastq.gz"%(homeDIR,sample), "%s/%s/%s.rmdup.HG19.bam"%(homeDIR,sample,sample),"%s/CopywriteR/CNAprofiles/%s_segment.output.txt"%(homeDIR,sample), "%s/CopywriteR/CNAprofiles/segment.Rdata"%(homeDIR),"%s/baf/%s.snp138_minR20_minMapQ15_minBaseQ20.baf"%(homeDIR,sample) ]	
	# copy analysis file
	for line in CopyList:
		#cpCMD = "cp %s %s"%(line,cpDIR)
		#print cpCMD
		#os.system(cpCMD)
		if os.path.isfile(line) == False : 
			print("file not found {0}".format(line))
			continue
		shutil.copy(line,cpDIR)
		
	# copy result list
	#CopyList = ["%s/decision_call.result"%homeDIR,"%s/EnfantGuard_plot.pdf"%homeDIR,"%s/ontarget.report"%homeDIR,"%s/issue.report"%homeDIR,"%s/ratio.report"%homeDIR,"%s/run.info"%homeDIR]
#	CopyList = ["%s/%s_decision_call.result"%(homeDIR,sample),"%s/EnfantGuard_plot.pdf"%homeDIR,"%s/ontarget.report"%homeDIR,"%s/ratio.report"%homeDIR]
	CopyList = ["%s/%s_decision_call.result"%(homeDIR,sample),"%s/%s_EnfantGuard_plot.pdf"%(homeDIR,sample),"%s/%s_ontarget.report"%(homeDIR,sample),"%s/%s_ratio.report"%(homeDIR,sample), "%s/%s_issue.report"%(homeDIR,sample)]
	# copy result file
	for line in CopyList:
		#cpCMD = "cp %s %s/result"%(line,cpDIR)
		#print cpCMD
		#os.system(cpCMDa)
		if os.path.isfile(line) == False :
			print("file not found {0}".format(line))
			continue
		shutil.copy(line,cpResultDIR)
	#compress
	os.chdir(homeDIR)
	CompCMD = "tar -zcvf %s@%s.tar.gz COMPtmp"%(sample,runid)
	print CompCMD
	os.system(CompCMD)
	
	#rmcpDirCMD = "rm -rf %s" %cpDIR
	#print rmcpDirCMD
	#os.system(rmcpDirCMD)
	try:
		shutil.rmtree(cpDIR)
	except OSError as ex:
		print(ex)

	os.chdir(initDIR)

def DeleteFile(runid,sample):
	
	initDIR = os.getcwd()
	
	homeDIR="%s/%s/%s" %(Analysis_dataDIR,runid,sample)
	
	DelList = ["%s/%s_yfraction_rd.bed"%(homeDIR,sample),"%s/%s"%(homeDIR,sample),"%s/baf"%homeDIR,"%s/bam"%homeDIR,"%s/contra"%homeDIR,"%s/decision_call.result2"%homeDIR,"%s/decision_call.result.orig"%homeDIR,"%s/decision_call.result.tmp"%homeDIR,"%s/EnfantGuard_plot.jpg"%homeDIR,"%s/FASTQ"%homeDIR,"%s/plot.jpg"%homeDIR,"%s/plot.pdf"%homeDIR,"%s/significant.list"%homeDIR,"%s/CopywriteR/segment.Rdata"%homeDIR, "%s/CopywriteR/segment.VS.control.data.txt"%homeDIR, "%s/CopywriteR/CNAprofiles/%s_segment.data.txt"%(homeDIR, sample), "%s/CopywriteR/CNAprofiles/%s_segment.output.old.txt"%(homeDIR, sample), "%s/CopywriteR/CNAprofiles/%s_segment.segRows.txt"%(homeDIR, sample), "%s/CopywriteR/CNAprofiles/CopywriteR.log"%homeDIR, "%s/CopywriteR/CNAprofiles/segment.Rdata"%homeDIR, "%s/CopywriteR/CNAprofiles/read_counts.txt"%homeDIR, "%s/CopywriteR/CNAprofiles/qc"%homeDIR, "%s/CopywriteR/CNAprofiles/plots"%homeDIR, "%s/CopywriteR/CNAprofiles/log2_read_counts.igv"%homeDIR, "%s/CopywriteR/CNAprofiles/input.Rdata"%homeDIR
]
	for line in DelList:
		cpCMD = "rm -rf %s"%line
		print cpCMD	
		os.system(cpCMD)
	
	os.chdir(initDIR)

	
def main(argv):
	start = time.time()
        print(len(argv))
	runid=argv[0]
	#sample=argv[1]
        sBackup_dir = argv[1]
        lsSample = []
        print("Backup {0}/{1}".format(Analysis_dataDIR, runid))
        if os.path.isdir("{0}/{1}".format(Analysis_dataDIR, runid)) == True : 
                lsSample = os.listdir("{0}/{1}/".format(Analysis_dataDIR, runid))
                for i in range(0, len(lsSample)) : 
                        sample = lsSample[i]
                        if os.path.isdir("{0}/{1}/{2}".format(Analysis_dataDIR, runid, sample)) == False : 
                                print("{0} is not directory".format(sample))
                                continue
	                CompFile = "%s/%s/%s/%s@%s.tar.gz" %(Analysis_dataDIR,runid,sample,sample,runid)
	
	                if os.path.isfile(CompFile):
                                #GenerationCOMP(runid,sample)
		                #DeleteFile(runid,sample)
		                print "exist CompFile"
	                else:
		                print "generating CompFile"
                                GenerationCOMP(runid,sample)
	                        #DeleteFile(runid,sample)
	
	                print "\n Elapsed Time: %s" % (time.time() - start)
        else : 
                print("run_id {0} don't exist".format(runid))
        sCp_CMD = "cp %s/%s/*/*.tar.gz %s" %(Analysis_dataDIR,runid,sBackup_dir)
        os.system(sCp_CMD)
    
if __name__ == "__main__":
    main(sys.argv[1:])
