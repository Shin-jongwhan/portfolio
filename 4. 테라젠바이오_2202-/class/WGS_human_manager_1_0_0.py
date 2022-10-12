import sys
import os


class WGS_manager : 
	def __init__(self) : 
		self.sample_config = {}

	
	def read_sample_config(self, sSample_config_file) : 
		fSample_config = open(sSample_config_file, 'r')
		for i in fSample_config : 
			i = i.replace("\n", "")
			if "#" in i : 
				continue
			if len(i.split("=")) != 2 : 
				print("Sample config can't parse accurately.")
				print("Check this line : \n", i)
				sys.exit()
			self.sample_config[i.split("=")[0].rstrip()] = i.split("=")[1].lstrip()
		fSample_config.close()

		return self.sample_config
