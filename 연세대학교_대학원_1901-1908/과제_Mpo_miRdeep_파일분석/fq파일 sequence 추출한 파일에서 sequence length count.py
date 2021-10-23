def main() :
    fExtract = open("D:\\NGS_data\\raw_data\\PhD_jung_hyunju\\0h.R1.clean.fq\\0h.R1.clean_extract_seq.txt", 'r')
    dicLength = {}
    nCount = 0
    while True :
        nCount += 1
        if nCount % 1000000 == 0 :
            print("{0} reads is counted".format(nCount))
        i = fExtract.readline()
        i = i.replace("\n", "")
        if i == "" :
            print("number of total reads : ", nCount - 1)
            break
        if len(i) in dicLength :
            dicLength[ len(i) ] += 1
            continue
        else :
            dicLength[ len(i) ] = 1
            continue
    
    nSum = 0
    for i in list(dicLength.keys()) :
        nSum += dicLength[i]
    print("total number of counted entire length : ", nSum)
    lsLength = sorted(dicLength.items())
    fExtract.close()
    fWrite = open("D:\\NGS_data\\raw_data\\PhD_jung_hyunju\\0h.R1.clean.fq\\0h.R1.clean_length.txt", 'w')
    for i in range(0, len(lsLength)) :
        fWrite.write(str(lsLength[i][0]))
        fWrite.write("\t")
        fWrite.write(str(lsLength[i][1]))
        fWrite.write("\n")
    fWrite.close()
    
main()
