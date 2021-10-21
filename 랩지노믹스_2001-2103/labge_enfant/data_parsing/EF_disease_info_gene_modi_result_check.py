### 309개 전부 있는 것 확인하였고, 엑셀에 있는 disease 목록도 다 있는 것으로 확인하였음. 그리고 gene은 그 질병의 gene에 있는 것도 확인하였음.


def main() :
    fDisease_test = open("C:\\Users\\user\\Desktop\\신종환_앙팡가드\\참고자료\\데이터\\disease_and_genes_in_EF_excel.txt", 'r')
    fRead = open("C:\\Users\\user\\Desktop\\신종환_앙팡가드\\참고자료\\데이터\\EnfantGouart_disease_info_genes_200305.txt", 'r', encoding = "utf-8")

    lsDisease = []
    lsRead = []

    while True :
        i = fDisease_test.readline().strip()
        if i != "" :
            lsDisease.append(i.split("\t"))
        else :
            break

    while True :
        i = fRead.readline().strip()
        if i != "" :
            lsRead.append(i.split("\t"))
        else :
            break

    print(len(lsDisease))
    print(len(lsRead))

    fDisease_test.close()
    fRead.close()

    nCount = 0
    for i in range(0, len(lsRead)) :
        for k in range(0, len(lsDisease)) :
            if len(lsRead[i]) == 14 : 
                sDisease = lsRead[i][-4][1:-1]
            else :
                sDisease = lsRead[i][-1][1:-1]
            if sDisease == lsDisease[k][0] and len(lsRead[i]) != 14 and len(lsDisease[k]) == 1 :
                #print("OK", lsDisease[k])
                #print(lsRead[i])
                nCount += 1
                continue
            elif sDisease == lsDisease[k][0] and len(lsRead[i]) == 14 and lsDisease[k][1] != "" :
                #print(lsDisease[k][1])
                if lsRead[i][-3] in lsDisease[k][1] :
                    #print("OK", lsDisease[k])
                    #print(lsRead[i])
                    nCount += 1
                    continue
                else :
                    print(lsRead[i])
                    print(lsDisease[k])
                    print()

    print(nCount)
    if nCount == len(lsRead) :
        print("All disease and genes exist in lsRead")
    else :
        print("Not all disease and genes exist in lsRead") 

main()
