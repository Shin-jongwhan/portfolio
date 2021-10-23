a = open("D:\\NGS_data\\PhD_jung_hyunju\\0h.R1.clean.fq\\0h.R1.clean.fq", 'r')
nCount_not_trim = 0

while True :
    i = a.readline()
    if "@" in i :
        k = a.readline()
        if len(k) >= 76 :
            nCount_not_trim += 1
            a.readline()
            a.readline()
    if "" == i :
        break
print("number of not tirimmed reads : ", nCount_not_trim)
