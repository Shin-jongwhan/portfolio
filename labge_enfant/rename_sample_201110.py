#!/usr/bin/python
# -*- coding:utf-8 -*-
import paramiko
import os


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# [shinejh0528@bros python]$ hostname -I
# 192.168.7.51 192.168.17.51 192.168.122.1
ssh_client.connect('192.168.7.51', username='lims', password='lims1324')
# commend execution ex) ssh_client.exec_command('commend')


def rename_sample() : 
        sRun_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/"

        fRename_sample_list = open("/data/Tools/bin/rename_sample_list.txt", 'r')

        print("run_id\tori_sample\trename_sample")
        for i in fRename_sample_list : 
                if "\t" not in i :      # error solving : if "\t" is going to space "    "
                        while True : 
                                if "  " in i : 
                                        i = i.replace("  ", " ")
                                else : 
                                        lsSample = i.strip().split(" ")
                                        break
                else : 
                        lsSample = i.strip().split("\t")        #[0] run_id [1] ori_sample [2] rename_sample
                print("\t".join(lsSample))
        
                lsPath = []
                for (path, dir, files) in os.walk(sRun_dir + "/".join(lsSample[:2]) + "/") : 
                        if path[-1] != "/" : 
                                lsPath.append(path + "/")
                        else : 
                                lsPath.append(path)

                lsPath.sort(key = lambda x : len(x.split("/")), reverse = True)
                
                for path in lsPath : 
                        print(path)
                        if "/".join(path.split("/")[-4:]) == "CopywriteR/CNAprofiles/plots/" : 
                                sSample_ori_tmp = lsSample[1].replace("-", ".")
                                sSample_rename_tmp = lsSample[2].replace("-", ".")
                                ssh_client.exec_command("cd {0} && rename {1} {2} *{3}*".format(path, sSample_ori_tmp, sSample_rename_tmp, sSample_ori_tmp))
                        else : 
                                ssh_client.exec_command("cd {0} && rename {1} {2} *{3}*".format(path, lsSample[1], lsSample[2], lsSample[1]))
                
                path = sRun_dir + lsSample[0] + "/"     # run_dir
                ssh_client.exec_command("cd {0} && rename {1} {2} *{3}*".format(path, lsSample[1], lsSample[2], lsSample[1]))
        
                print("")

        fRename_sample_list.close() 


def main() : 
        rename_sample()


main()
ssh_client.close()
