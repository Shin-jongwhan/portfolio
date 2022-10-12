import sys
import os


class vcf_parser : 
	def __init__(self) : 
		self.meta_info = []
		self.header = []
		self.variants = []

	
	def read_vcf(self, sVcf_file) : 
		fVcf = open(sVcf_file, 'r')
		lsVcf = fVcf.read().split("\n")
		fVcf.close()
		if lsVcf[-1] == "" : 
			del lsVcf[-1]

		for i in range(0, len(lsVcf)) : 
			if "##" == lsVcf[i][:2] : 
				self.meta_info.append(lsVcf[i])
			elif "#" == lsVcf[i][0] and "##" != lsVcf[i][:2] : 
				self.header.append(lsVcf[i][1:].split("\t"))
			else : 
				self.variants.append(lsVcf[i].split("\t"))
