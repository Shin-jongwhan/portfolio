a = open("D:\\NGS_data\\PhD_jeong_hyunju\\2019HC039_small_20190405010442\\24h.R1.fq", 'r')
b = []
fWrite = open("D:\\NGS_data\\PhD_jeong_hyunju\\2019HC039_small_20190405010442\\24h.R1.trim.fq", 'w')


while True :
    k = a.readline()
    if "@" in k :
        i = a.readline()
        if len(i) < 15 :
            a.readline()
            a.readline()
            continue
        #  "TGGAATTCTCGG" : (RNA ---- ) speculated P5 primer( ---- barcode ---- P7 primer)
        if "TGGAATTCTCGG" in i :
            fWrite.write(k)
            fWrite.write(i[0 : i.find("TGGAATTCTCGG")])
            fWrite.write("\n")
            fWrite.write(a.readline())
            fWrite.write(a.readline()[0:i.find("TGGAATTCTCGG")])
            fWrite.write("\n")
        elif "TGGAATTCTCGG" not in i :
            a.readline()
            a.readline()
            continue
    else :
        print("순서 오류 or 완료")
        print(k)
        break
    
fWrite.close()
a.close()
