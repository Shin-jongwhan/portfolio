#!/usr/bin/python
# -*- coding:utf-8 -*-
import os, sys
import time
#import MySQLdb
import requests
import json,urllib

os.environ['http_proxy'] = 'http://192.168.7.12:3128/'
os.environ['https_proxy'] = 'http://192.168.7.12:3128/'
os.environ['ftp_proxy'] = 'http://192.168.7.12:3128/'

key="2C2CB8ED-6D69-457C-981C-8C7CFC24A3E7"


def sample_list() : 
        sRun_dir = "/data/Analysis/Project/EnfantGuard/Analysis_data/"
        lsRun_id = []
        for i in os.listdir(sRun_dir) :
                #print(i)
                if len(i.split("_")) != 4 :
                        continue
                #print(i)
                #print(i[:2])
                if "NS" in i or "NB" in i or "NDX" in i :
                        if i[:2] == "16" or i[:2] == "17" : 
                                continue
                        #print(i)
                        if os.path.isdir(sRun_dir + i) : 
                                lsRun_id.append(i)
                                print(i)

        lsSample = []
        nSample_count = 0
        for i in range(0, len(lsRun_id)) : 
                for sSample in os.listdir(sRun_dir + lsRun_id[i] + "/") : 
                        if os.path.isdir(sRun_dir + lsRun_id[i] + "/" + sSample) :
                                ########################################################
                                # check file
                                if "Father" in sSample or "Mother" in sSample or "_" in sSample :
                                        continue
                                elif len(sSample.split("-")[0]) != 13 :
                                        continue
                                elif "TEST" in sSample or "test" in sSample : 
                                        continue
                                lsSample.append(sSample)
                                #print(sSample)
                                nSample_count += 1
                                #time.sleep(0.003)
        print("Number of sample : {0}".format(nSample_count))

        return lsSample


def call_DB(lsSample) : 
        #sample = "2020050230320-EF3-LT-LR-Merged"
        for sample in lsSample : 
                print(sample)
                id = sample[:13]

                js_url = "http://labge02:8080/enfantguard/api/enfantguard/%s/%s?key=%s" %(id,sample,key)
                #print(js_url)
                data = urllib.urlopen(js_url).read()
                try : 
                        js_data = json.loads(data)
                except : 
                        print("{0} is not a sample or don't sexist in DB".format(sample))
                        continue
                #print(js_data)

                #print(type(js_data))
                #print(js_data.keys())
                lsKey_js_data = list(js_data.keys())
                
                lsIssue_Sent_result = []

                for i in range(0, len(js_data["sample"]["issue"])) : 
                        sIssue_contents = js_data["sample"]["issue"][i]["contents"]
                        sIssue_contents = u"{0}".format(sIssue_contents)
                        if u"샘플 분석결과 랩센터 전송" in sIssue_contents and ":" in sIssue_contents :         # 양성 가능성
                                #print(sIssue_contents[sIssue_contents.find(u"송") + 2])
                                print(sIssue_contents)
                                sContents = sIssue_contents[ (sIssue_contents.find(u"송") + 2) :]
                                if "->" not in sContents and u"정상" in sContents : 
                                        print("정상\n{0}".format(sContents))
                                elif "->" in sContents : 
                                        if u"정상" in sContents.split("->")[1] : 
                                                print("정상\n{0}".format(sContents))
                                        elif u"정상" not in sContents.split("->")[1] : 
                                                print("비정상\n{0}".format(sContents))
                                #if u"정상" in sIssue_contents.split(":")[1] : 
                                #        print(u"정상 {0}".format(sIssue_contents))
                                #print("sadfasdfasdf" + ":".join(sIssue_contents.split(":")[1:]) + "\n\n")
                                #if u"정상" not in sIssue_contents.split(":")[1] : 
                                #        print(u"{0}".format(sIssue_contents))
                                #print(sIssue_contents.split("->")[1])
                
                ################################################
                # test
                #print("")
                #print(js_data["sample"]["issue"][4]["contents"])
                #lsTest = js_data["sample"]["issue"][4]["contents"].split("->")
                #print(lsTest[1])
                ################################################


def main() : 
        lsSample = sample_list()
        call_DB(lsSample)


main()
