# find barcode and find RNA sequence
fFile = open("D:\\NGS_data\\PhD_jung_hyunju\\2019HC039_small_20190405010442\\0h.R1.fq", 'r')
fWrite = open("D:\\NGS_data\\PhD_jung_hyunju\\2019HC039_small_20190405010442\\0h_barcode_test.fq", 'w')
#nRead_num = 0

while True :
    i = fFile.readline()
    if "TAATCG" in i :
        #nRead_num += 1
        fWrite.write(i[ i.find("TAATCG") + 6 : ])
    if i == "" :
        break
fFile.close()
fWrite.close()
