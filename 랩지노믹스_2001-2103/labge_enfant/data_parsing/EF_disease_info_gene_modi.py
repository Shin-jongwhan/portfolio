# EnfantGaurd_disease_gene.txt 의 gene 목록을 modification
# 영역 겹치는 유전자 모두 제거하고 가장 영역 큰 것만 남기기
# 앙팡가드 엑셀에 있는 중요 유전자 목록 모두 수기로 확인하였고(245개), 질병 147개 수 일치하고 있는지 모두 확인하였음.
"""
### print output
lsNot_exist_disease()
All diseases exist.
len(lsGenes) 146
Number of not existed genes (0 is means that the file have all genes) :  0
[14, 11]
len(lsGene) 138
len(lsDisease1) 247
len(lsDisease2) 247
nCount_gene_num 146
len(lsRead3) 309
len(lsDisease) 247
len(lsGene) 138
"""

import numpy as np


def check_disease_list() :
    fDisease_info = open("C:\\Users\\user\\Desktop\\신종환_앙팡가드\\참고자료\\데이터\\EnfantGuard.ver3.info", 'r', encoding = "utf-8")
    fRead = open("C:\\Users\\user\\Desktop\\신종환_앙팡가드\\참고자료\\데이터\\EnfantGaurd_disease_gene.txt", 'r', encoding = "utf-8")

    lsDisease_info = []
    lsRead = []

    while True :
        i = fDisease_info.readline().strip()
        if i != "" :
            lsDisease_info.append(i.split("\t"))
        else : break
    fDisease_info.close()

    while True :
        i = fRead.readline().strip()
        if i != "" :
            lsRead.append(i.split("\t"))
        else : break
    fRead.close()

    lsNot_exist_disease = []
    for i in range(0, len(lsDisease_info)) :
        bool_exist = False
        for k in range(0, len(lsRead)) :
            if i != len(lsRead) - 1 : 
                if lsDisease_info[i][3] == lsRead[k][3] :
                    bool_exist = True
            else :
                if bool_exist == False and lsDisease_info[i][3] == lsRead[k][3] :
                    lsNot_exist_disease.append(lsRead[k])
                elif bool_exist == True :
                    continue
        bool_exist = False
                
    print("lsNot_exist_disease()")
    if len(lsNot_exist_disease) >= 2 :
        for i in range(0, len(lsNot_exist_disease)) :
            print(lsNot_exist_disease[i])
    elif len(lsNot_exist_disease) == 1 :
        print(lsNot_exist_disease[0])
    else :
        print("All diseases exist.")
            


def pick_region(lsRegion) :
    for k in range(len(lsRegion) - 1, 0, -1) :
        if int(lsRegion[k][-2]) <= int(lsRegion[k - 1][-2]) and int(lsRegion[k][-1]) >= int(lsRegion[k - 1][-1]) :
            del lsRegion[k - 1]
        elif int(lsRegion[k][-2]) >= int(lsRegion[k - 1][-2]) and int(lsRegion[k][-1]) <= int(lsRegion[k - 1][-1]) :
            del lsRegion[k]
        elif ( int(lsRegion[k][-2]) >= int(lsRegion[k - 1][-2]) and int(lsRegion[k][-2]) <= int(lsRegion[k - 1][-1]) ) or ( int(lsRegion[k][-2]) <= int(lsRegion[k - 1][-2]) and int(lsRegion[k][-1]) >= int(lsRegion[k - 1][-2]) ) :
            nWhole_region_start = min(int(lsRegion[k][-2]), int(lsRegion[k - 1][-2]))
            nWhole_region_end = max(int(lsRegion[k][-1]), int(lsRegion[k - 1][-1]))
            nOverlap_start = max(int(lsRegion[k][-2]), int(lsRegion[k - 1][-2]))
            nOverlap_end = min(int(lsRegion[k][-1]), int(lsRegion[k - 1][-1]))
            if (nOverlap_end - nOverlap_start) / (nWhole_region_end - nWhole_region_start) > 0.3 :
                lsRegion[k][-2] = str(min(int(lsRegion[k][-2]), int(lsRegion[k - 1][-2])))
                lsRegion[k][-1] = str(max(int(lsRegion[k][-1]), int(lsRegion[k - 1][-1])))
                del lsRegion[k - 1]
        elif int(lsRegion[k][-2]) >= int(lsRegion[k - 1][-1]) or int(lsRegion[k][-1]) <= int(lsRegion[k - 1][-2]) :
            continue
    if len(lsRegion) >= 2 :     # if still len(lsRegion) >= 1, re-test
        for i in range(len(lsRegion) - 1, 0, -1) :
            for k in range(len(lsRegion) - 1, 0, -1) :
                if ( int(lsRegion[i][-2]) >= int(lsRegion[k][-2]) and int(lsRegion[i][-2]) <= int(lsRegion[k][-1]) ) or ( int(lsRegion[i][-2]) <= int(lsRegion[k][-2]) and int(lsRegion[i][-1]) >= int(lsRegion[k][-2]) ) :
                    nWhole_region_start = min(int(lsRegion[i][-2]), int(lsRegion[k][-2]))
                    nWhole_region_end = max(int(lsRegion[i][-1]), int(lsRegion[k][-1]))
                    nOverlap_start = max(int(lsRegion[i][-2]), int(lsRegion[k][-2]))
                    nOverlap_end = min(int(lsRegion[i][-1]), int(lsRegion[k][-1]))
                    if (nOverlap_end - nOverlap_start) / (nWhole_region_end - nWhole_region_start) > 0.3 :
                        lsRegion[i][-2] = str(min(int(lsRegion[i][-2]), int(lsRegion[k][-2])))
                        lsRegion[i][-1] = str(max(int(lsRegion[i][-1]), int(lsRegion[k][-1])))
                        del lsRegion[k]
                        break
                    
    return lsRegion


def sort_disease_list(lsRead3) :
    lsChr = []
    for i in range(0, 25) :
        if i < 23 :
            lsChr.append("chr%d" % i)
        elif i == 23 :
            lsChr.append("chrX")
        elif i == 24 :
            lsChr.append("chrY")
    
    
            
    

def main() :
    check_disease_list()

    fRead = open("C:\\Users\\user\\Desktop\\신종환_앙팡가드\\참고자료\\데이터\\EnfantGaurd_disease_gene.txt", 'r', encoding = "utf-8")
    lsRead = []
    lsRength = []
    while True :
        i = fRead.readline()
        if i != "" :
            i = i.strip().split("\t")
            if len(i) not in lsRength :
                lsRength.append(len(i))
            lsRead.append(i)
        else :
            break
    fRead.close()

    ###############################################
    ### genes list check
    fGenes = open("C:\\Users\\user\\Desktop\\신종환_앙팡가드\\참고자료\\데이터\\genes_in_EF_excel.txt", 'r')
    lsGenes = []
    while True :
        i = fGenes.readline().strip().replace(" ", "")
        if i != "" :
            i = i.split(",")
            if len(i) > 1 :
                for k in range(0, len(i)) :
                    lsGenes.append(i[k])
            else :
                lsGenes.append(i[0])
        else :
            break
    print("len(lsGenes)", len(lsGenes))
    fGenes.close()

    nCount_not_exist_gene = 0
    for i in range(0, len(lsGenes)) :
        #print(lsGenes[i])
        for k in range(0, len(lsRead)) :
            if k != len(lsRead) - 1 : 
                if len(lsRead[k]) == 14 and lsGenes[i] == lsRead[k][-3] :
                    break
            else :
                if len(lsRead[k]) == 14 and lsGenes[i] == lsRead[k][-3] :
                    break
                else :
                    nCount_not_exist_gene += 1
                    print("Do not exist this gene in EnfantGaurd_disease_gene.txt : ", lsGenes[i])
    print("Number of not existed genes (0 is means that the file have all genes) : ", nCount_not_exist_gene)

    ###############################################

    print(lsRength)
    lsGene = []
    for i in range(0, len(lsRead)) :
        if len(lsRead[i]) == 14 and lsRead[i][-3] not in lsGene :
            lsGene.append(lsRead[i][-3])
            #print(lsGene[-1])
    print("len(lsGene)", len(lsGene))

    # for check
    lsDisease1 = []
    for i in range(0, len(lsRead)) :
        if lsRead[i][3] not in lsDisease1 :
            lsDisease1.append(lsRead[i][3])
            #print(lsDisease[-1])
    print("len(lsDisease1)", len(lsDisease1))

    ### modi #1
    for i in range(len(lsRead) - 1, 0, -1) :
        if len(lsRead[i]) == 14 and len(lsRead[i - 1]) == 14 and lsRead[i][-3] == lsRead[i - 1][-3] and lsRead[i][-2] == lsRead[i - 1][-2] and lsRead[i][-1] == lsRead[i - 1][-1] and lsRead[i][3] == lsRead[i - 1][3] :
            del lsRead[i]

    # for check
    lsDisease2 = []
    for i in range(0, len(lsRead)) :
        if lsRead[i][3] not in lsDisease2 :
            lsDisease2.append(lsRead[i][3])
            #print(lsDisease[-1])
    print("len(lsDisease2)", len(lsDisease2))

    #for i in range(0, len(lsDisease1)) :
    #    if lsDisease1[i] not in lsDisease2 :
    #        print(lsDisease1[i])

    #for i in range(0, len(lsRead)) :
    #    print(lsRead[i])
    
    ### modi #2
    lsRead2 = []
    lsRegion = []
    lsDel_list = []
    lsError_check = []
    #lsDisease3 = []        # for check
    sDisease = ""
    for i in range(0, len(lsRead)) :
        if i == 0 :
            sDisease = lsRead[i][3]
            if sDisease == lsRead[i + 1][3] :
                if lsRead[i][-3] == lsRead[i + 1][-3] :
                    lsRegion.append(lsRead[i])
                else :
                    lsRead2.append(lsRead[i])
            else :
                lsRaed2.append(lsRead[i])
                sDisease = lsRead[i + 1][3]
        elif i != 0 and i != len(lsRead) - 1 :
            if sDisease == lsRead[i + 1][3] :
                if lsRead[i][-3] == lsRead[i + 1][-3] :
                    lsRegion.append(lsRead[i])
                else :
                    if len(lsRegion) >= 1 :
                        lsRegion.append(lsRead[i])
                        lsRegion = pick_region(lsRegion)
                        for k in range(0, len(lsRegion)) :
                            lsRead2.append(lsRegion[k])
                        lsRegion = []
                    #if end
                    elif len(lsRegion) == 0 :
                        lsRead2.append(lsRead[i])
            #if end
            else :
                sDisease = lsRead[i + 1][3]
                if len(lsRegion) >= 1 :
                    lsRegion.append(lsRead[i])
                    lsRegion = pick_region(lsRegion)
                    for k in range(0, len(lsRegion)) :
                        lsRead2.append(lsRegion[k])
                    lsRegion = []
                #if end
                else : 
                    lsRead2.append(lsRead[i])
        elif i == len(lsRead) - 1 :
            if sDisease == lsRead[i - 1][3] :
                if lsRead[i][-3] == lsRead[i - 1][-3] :
                    lsRegion.append(lsRead[i])
                    lsRegion = pick_region(lsRegion)
                    for k in range(0, len(lsRegion)) :
                        lsRead2.append(lsRegion[k])
                else :
                    lsRead2.append(lsRead[i])
            else :
                lsRead2.append(lsRead[i])

                
    lsRead3 = []
    for i in range(len(lsRead2) - 1, -1, -1) :
        for k in range(0, len(lsRead)) :
            if lsRead2[i][-3] == lsRead[k][-3] :
                if "".join(lsRead2[i]) == "".join(lsRead[k]) :
                    lsRead3.append(lsRead[k])
                    break

    lsDisease = []
    lsGene = []
    nCount = 0
    for i in range(0, len(lsRead3)) :
        if lsRead3[i][3] not in lsDisease :
            lsDisease.append(lsRead3[i][3])
            #print(lsDisease[-1])
        if len(lsRead3[i]) == 14 and lsRead3[i][-3] not in lsGene :
            lsGene.append(lsRead3[i][-3])
        if len(lsRead3[i]) == 14 : 
            nCount += 1
    print("nCount_gene_num", nCount)
    #for i in range(0, len(lsError_check)) :
    #    if lsError_check[i][3] not in lsDisease :
    #        print(lsError_check[i])
    print("len(lsRead3)", len(lsRead3))
    print("len(lsDisease)", len(lsDisease))
    print("len(lsGene)", len(lsGene))
    print()
    print()

    fResult = open("C:\\Users\\user\\Desktop\\EnfantGouart_disease_info_genes_modi.txt", 'w', encoding = "utf-8")
    for i in range(0, len(lsRead3)) :
        if len(lsRead3[i]) == 14 : 
            fResult.write("\t".join(lsRead3[i]) + "\n")
    fResult.close()
    
    
            
        
        
main()
