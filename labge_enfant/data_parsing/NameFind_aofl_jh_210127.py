#!/usr/bin/python
import MySQLdb
import os,sys
import requests
import json,urllib
import pandas as pd
import datetime, time
key="2C2CB8ED-6D69-457C-981C-8C7CFC24A3E7"
reload(sys)
sys.setdefaultencoding('utf-8')

def Find_Name(sample):

        os.environ['http_proxy'] = 'http://192.168.7.12:3128/'
        os.environ['https_proxy'] = 'http://192.168.7.12:3128/'
        os.environ['ftp_proxy'] = 'http://192.168.7.12:3128/'

        id = sample[:13]
        sampleToken = sample.split("-")
        EF = sampleToken[1]
        LT = sampleToken[2]
        if len(sampleToken) == 5:
                LR1 = sampleToken[3]
                LR2 = sampleToken[4]
        elif len(sampleToken) == 4:
                LR1 = sampleToken[3]
                LR2 = "NA"
        else:
                LR1 = "NA"
                LR2 = "NA"
        id8 = id[:8]
        id5 = id[8:]
        name = "NULL"

        if LT[-1] == "\n":
            LT = LT[:-1]
        elif LR1[-1] == "\n":
            LR1 = LR1[:-1]
        elif LR2[-1] == "\n":
            LR2 = LR2[:-1]

        if LR1 == "LR2" and LR2 == "NA":
            LR1 = "LR"
            LR2 = "LR"
        elif LR1 == "SR2" and LR2 == "NA":
            LR1 = "SR"
            LR2 = "SR"

        sample=sample.strip()
        js_url = "http://labge02:8080/enfantguard/api/enfantguard/%s/%s?key=%s" %(id,sample,key)
        #print js_url
        #js_url = "http://labge02/enfantguard/api/enfantguard/%s/%s" %(id,sample)

        data = urllib.urlopen(js_url).read()
        js_data = json.loads(data)
        name = js_data["sample"]["initial"]
        sex = js_data["sample"]["sex"]
        pre = js_data["pre"]
        hyb = js_data["hyb"]
        post = js_data["post"]
        RunID = js_data["runId"]
        #print name
        #print RunID
        #ProxyHTTPCMD = "export -n http_proxy=http://192.168.7.12:3128/"
        #ProxyHTTPSCMD = "export -n https_proxy=http://192.168.7.12:3128/"
        #ProxyFTPCMD = "export -n ftp_proxy=http://192.168.7.12:3128/"

        #os.system(ProxyHTTPCMD)
        #os.system(ProxyHTTPSCMD)
        #os.system(ProxyFTPCMD)

        return id8, id5, EF,LT, LR1, LR2, name,pre,hyb,post,sex,RunID

def main(argv):
        Series_List =[]
        NameFileName=argv[0]
        fSample_data = open("/home/shinejh0528/sample_data.txt", 'w')
        with open(NameFileName, 'r') as NameFile:
                for sample in NameFile:
                        #print(sample)
                        row =[]
                        sample.strip()
                        if len(sample.split("-")[0]) != 13 : 
                                continue
                        if "TEST" in sample : 
                                continue
                        id8,id5,EF,LT,LR1,LR2,name,pre,hyb,post,sex,RunID=Find_Name(sample)
                        row = [id8,id5,EF,LT,LR1,LR2,name,pre,hyb,post,sex,RunID]
                        Series_List.append(pd.Series(row))
			d = datetime.date.today()
                        try : 
                                fSample_data.write(RunID + '/' + id8+id5+'-'+EF+'-'+LT + '/' + str(d.isoformat().replace('-','')) + '/' + id8 + '/' + id5 + '/' +EF + '/' + LT + '/' + LR1 + '/' + LR2 + '/' +name + '/' + 'NA' + '/' +sex + '/' +pre + '/' +hyb + '/' +post + "\n")
                        except : 
                                print("sample_data write none type error")
			#print RunID + '/' + id8+id5+'-'+EF+'-'+LT + '/' + str(d.isoformat().replace('-','')) + '/' + id8 + '/' + id5 + '/' +EF + '/' + LT + '/' + LR1 + '/' + LR2 + '/' +name + '/' + 'NA' + '/' +sex + '/' +pre + '/' +hyb + '/' +post
#                        print "%s/%s/%s/%s/%s/%s/%s/NA/%s/%s/%s/%s/%s"%(id8, id5,EF, LT, LR1, LR2,name,sex,RunID,pre,hyb,post)
        fSample_data.close()
        DF = pd.DataFrame(Series_List)
#       print DF
        #DF.to_csv("%s_output.csv"%(RunID), sep='\t', encoding='utf-8')

if __name__ == "__main__":
    main(sys.argv[1:])

