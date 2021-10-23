import os
import sys
import glob

sSample_list_dir = "/data/Analysis/ETC/enfant_call_test_171228/1.Data/200901_sample_test/"

fSample_list = open("/home/shinejh0528/etc/enfant_update/sample_list_folder_n_file_check_list.txt", 'r')

lsSample_list = fSample_list.readlines()
fSample_list.close()

for i in range(0, len(lsSample_list)) : 
        lsSample_list[i] = lsSample_list[i].strip()
        if os.path.isdir(sSample_list_dir + lsSample_list[i]) == True : 
                lsFile_list = glob.glob(sSample_list_dir + lsSample_list[i] + "/*")
                #print(len(lsFile_list))
                if len(lsFile_list) != 5 : 
                        print(lsSample_list[i])

        else : 
                print("no such sample", lsSample_list[i])




