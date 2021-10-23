a = open("D:\\NGS_data\\raw_data\\PhD_jung_hyunju\\miRDeep_analysis_result\\analysisData.190530\\0h\\0h.R1.clean.purify.fa", 'r')
b = {}
while True :
    i = a.readline()
    if i == "" :
        break
    if ">" in i :
        k = a.readline()
        k = k.replace("\n", "")
        if len(k) in b :
            b[len(k)] += 1
        else :
            b[len(k)] = 1

for i in list(b.keys()) :
    print(i, b[i])
