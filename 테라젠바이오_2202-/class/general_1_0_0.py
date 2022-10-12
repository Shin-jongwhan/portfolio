import sys
import os
import re
import time


class general : 
	def mkdir_cmd(self, sDir) : 
		if os.path.isdir(sDir) == False :
			sMkdir_cmd = "mkdir -p {0}".format(sDir)
			print(sMkdir_cmd)
			print("")
			os.system(sMkdir_cmd)


	def sh_command_exe(self, command) : 
		print(command)
		os.system(command)


	def clean_text(self, inputString):
		# This will convert special symbols to '_'
		text_rmv = re.sub('[^a-zA-Z0-9-_]', '_', inputString)
		#print(text_rmv)

		return text_rmv


	def ssh_get(self, user, server, pwd, port) :
		cli = paramiko.SSHClient()
		cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
		cli.connect(server, port=port, username=user, password=pwd)

		return cli


	def ssh_command_outpit_to_list(self, cli, sCommand) : 
		stdin, stdout, stderr = cli.exec_command(sCommand)
		time.sleep(4)		# for waiting to store the result
		lsStdout = stdout.readlines()
		lsStdout = [ lsStdout[i].replace("\n", "") for i in range(0, len(lsStdout)) ]


	def sh_conda_init(self, fSh) :		# conda init
		lsConda_init =[
		"__conda_setup=\"$(\'/TBI/People/tbi/jhshin/miniconda3/bin/conda\' \'shell.bash\' \'hook\' 2> /dev/null)\"",
		"if [ $? -eq 0 ]; then",
		"\teval \"$__conda_setup\"",
		"else",
		"\tif [ -f \"/TBI/People/tbi/jhshin/miniconda3/etc/profile.d/conda.sh\" ]; then",
		"\t\t. \"/TBI/People/tbi/jhshin/miniconda3/etc/profile.d/conda.sh\"",
		"\telse",
		"\t\texport PATH=\"/TBI/People/tbi/jhshin/miniconda3/bin:$PATH\"",
		"\tfi",
		"fi",
		"unset __conda_setup\n\n"
		]

		fSh.write("\n".join(lsConda_init))


	def get_max_storage_2_7(self) :
		# get max storage from data02 to 07
		lsStorage = os.popen("df").read().split("\n")
		del lsStorage[-1]		# null index
		lsMax_storage = []
		for i in range(0, len(lsStorage)) :
			for iter in range(0, 50) :
				lsStorage[i] = lsStorage[i].replace("  ", " ")
			lsStorage[i] = lsStorage[i].split(" ")
			if "/data02" == lsStorage[i][5] or "/data03" == lsStorage[i][5] or "/data04" == lsStorage[i][5] or "/data05" == lsStorage[i][5] or "/data06" == lsStorage[i][5] or "/data07" == lsStorage[i][5] :
				if lsMax_storage == [] :
					lsMax_storage = lsStorage[i]
				else :
					if int(lsMax_storage[3]) < int(lsStorage[i][3]) :
						lsMax_storage = lsStorage[i]
				#print(lsStorage[i])
		print("max storage\n", lsMax_storage)
	
		return lsMax_storage


	def get_max_storage_2_9(self) :
		# get max storage from data02 to 07, data09
		lsStorage = os.popen("df").read().split("\n")
		del lsStorage[-1]		# null index
		lsMax_storage = []
		for i in range(0, len(lsStorage)) :
			for iter in range(0, 50) :
				lsStorage[i] = lsStorage[i].replace("  ", " ")
			lsStorage[i] = lsStorage[i].split(" ")
			if "/data02" == lsStorage[i][5] or "/data03" == lsStorage[i][5] or "/data04" == lsStorage[i][5] or "/data05" == lsStorage[i][5] or "/data06" == lsStorage[i][5] or "/data07" == lsStorage[i][5] or "/data09" == lsStorage[i][5]:
				if lsMax_storage == [] :
					lsMax_storage = lsStorage[i]
				else :
					if int(lsMax_storage[3]) < int(lsStorage[i][3]) :
						lsMax_storage = lsStorage[i]
				#print(lsStorage[i])
		print("max storage\n", lsMax_storage)

		return lsMax_storage
