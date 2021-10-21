#!/usr/bin/python
# -*- coding:utf-8 -*-
import paramiko
import os

#sWork_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/201106_NDX550181_0185_AHK5N7AFX2/2020110460001-EF3-LT/CopywriteR/CNAprofiles/"
sWork_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/201106_NDX550181_0185_AHK5N7AFX2/"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# you can check in linux shell through tyrping $ hostname -I
# [shinejh0528@bros python]$ hostname -I
# 192.168.7.51 192.168.17.51 192.168.122.1
ssh_client.connect('192.168.7.51', username='lims', password='lims1324')

#not working
#channel = ssh_client.invoke_shell()
#channel.send('rename {0}2020110460001-EF3-LT {1}2020110460001-EF3-LT-rename {2}2020110460001-EF3-LT*'.format(sWork_dir, sWork_dir, sWork_dir))

#working
ssh_client.exec_command('rename {0}2020110460001-EF3-LT {1}2020110460001-EF3-LT-rename {2}2020110460001-EF3-LT*'.format(sWork_dir, sWork_dir, sWork_dir))

ssh_client.close()

#stdin, stdout, stderr = ssh_client.exec_command('ls')
#print stdout.read()









#def main():
#        ssh_client = None
#        recv_size = 9999
#
#        try:
#                ssh_client = paramiko.SSHClient()
#                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # host keys 관련 설정
#                ssh_client.connect('127.0.0.1', username='lims', password='lims1324')
#
#                channel = ssh_client.invoke_shell()
#                channel.send('su -\n')
#                outdata, errdata = waitStrems(channel)
#                print(outdata)
#        
#        finally : 
#                if ssh_client is not None:
#                        ssh_client.close()
#
#
#def waitStrems(chan):
#        outdata=errdata = ""
#        while chan.recv_ready():
#                outdata += chan.recv(1000)
#        while chan.recv_stderr_ready():
#                errdata += chan.recv_stderr(1000)
#        return outdata, errdata
#
#
#main()

