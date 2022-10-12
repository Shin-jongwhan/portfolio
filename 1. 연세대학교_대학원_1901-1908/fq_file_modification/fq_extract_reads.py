a = open("D:\\NGS_data\\raw_data\\PhD_jung_hyunju\\0h.R1.clean.fq\\0h.R1.clean.fq", 'r')
fWrite = open("D:\\NGS_data\\raw_data\\PhD_jung_hyunju\\0h.R1.clean.fq\\0h.R1.clean_extract_seq.txt", 'w')

while True :
    i = a.readline()
    if "@" in i :
        i = a.readline()
        fWrite.write(i)
        a.readline()
        a.readline()
        continue
    else :
        break

a.close()
fWrite.close()
