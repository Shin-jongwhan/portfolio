a = open("D:\\NGS_data\\raw_data\\PhD_jung_hyunju\\miRDeep_analysis_result\\analysisData.190530\\0h\\0h.read.length.txt", 'r')
b = {}
while True :
    i = a.readline()
    if i == "" :
        break
    i = i.replace("\n", "")
    if int(i) in b :
        b[int(i)] += 1
    else :
        b[int(i)] = 1

a.close()

b = sorted(b.items())
for i in range(0, len(b)) :
    print(b[i])
