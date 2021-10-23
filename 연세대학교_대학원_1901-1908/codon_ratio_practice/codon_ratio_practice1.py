import sys
## sys.exit(1) >> 프로그램 중간에 종료하고 싶을 때 씀
#해결사항: seq에 N R Y K M S W 있으면 다른 곳에 저장하도록 하는 것. 나중에 하기
#lsNuc = ["N", "R", "Y", "K", "M", "S", "W"]
#dicCodon_others = {}

def count_codon() :
    filename = input(str("Type which file you wanna open in Desktop location( ex) 과제\\~): "))
    print("Your file name is: ", filename)
    fGene = open("C:\\Users\\Shin\\Desktop\\{0}".format(filename), 'r')
    sGene = fGene.read()
    fGene.close()       #close file
    #sGene에 ATCG 이외의 bp 있는지 확인
    if not "A"in sGene :
        print("There exist not ATCG: ", i)
        sys.exit(1)
    elif not "T" in sGene :
        print("There exist not ATCG: ", i)
        sys.exit(1)
    elif not "C" in sGene :
        print("There exist not ATCG: ", i)
        sys.exit(1)
    elif not "G" in sGene :
        print("There exist not ATCG: ", i)
        sys.exit(1)
    #if not "A" or "T" or "C" or "G" in sGene :
        #print("There exist not kind of ATCG")
        #sys.exit(1)
    
    #gene sequence가 3의 배수가 아니라면 program break
    if not len(sGene) % 3 == 0 :
        print("Your gene sequence is not triplets")
        sys.exit(1)
    nCodon_num = int( len(sGene) / 3 )
    print("A number of codon is: ", nCodon_num)

    lsNuc = ["A", "T", "C", "G"]
    dicCodon = {}
    #Initialize triplet codon
    for i in lsNuc :
        for j in lsNuc :
            for k in lsNuc :
                dicCodon[i + j + k] = 0
    #for check
    #print("triplet codon: ", dicCodon)
    #count triplet codon
    for i in range(0, nCodon_num) :
        dicCodon[ sGene[ (i * 3) : ( (i * 3) + 3) ] ] += 1
    #for check
    print("counted number of triplet codon: ", dicCodon)

    return dicCodon, filename

def main() :
    dicCodon, filename = count_codon()
    dicCodon_ratio = {}
    #for check
    #print("this codon derived from main function: ", dicCodon)
    #codon list and initialize number of codon [-1]
    ######################기본 틀 
    #>>> dicAsn = {"AAT" : 5, "AAC" : 12}
    #>>> dicAsn["AAA"] = 10
    #>>> lsAsn = ["AAT", "AAC", 0]
    #>>> for i in dicAsn :
    #        if i in lsAsn :
    #                print("true", i, dicAsn[i])
    #                lsAsn[-1] += dicAsn[i]
    #        else :
    #                print("false", i , dicAsn[i])
    ######################
    lsAla = ["GCT", "GCC", "GCA", "GCG", 0]
    lsArg = ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG", 0]
    lsAsn = ["AAT", "AAC", 0]
    lsAsp = ["GAT", "GAC", 0]
    lsCys = ["TGT", "TGC", 0]
    lsGln = ["CAA", "CAG", 0]
    lsGlu = ["GAA", "GAG", 0]
    lsGly = ["GGT", "GGC", "GGA", "GGG", 0]
    lsHis = ["CAT", "CAC", 0]
    lsIle = ["ATT", "ATC", "ATA", 0]  #Upper i, lower L and e
    #lsStart = ["ATG"]
    lsLeu = ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG", 0]
    lsLys = ["AAA", "AAG", 0]
    lsMet = ["ATG", 0]
    lsPhe = ["TTT", "TTC", 0]
    lsPro = ["CCT", "CCC", "CCA", "CCG", 0]
    lsSer = ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC", 0]
    lsThr = ["ACT", "ACC", "ACA", "ACG", 0]
    lsTrp = ["TGG", 0]
    lsTyr = ["TAT", "TAC", 0]
    lsVal = ["GTT", "GTC", "GTA", "GTG", 0]
    lsStop = ["TAA", "TGA", "TAG", 0]
    
    #count codon to match a.a
    for i in dicCodon :
        if i in lsAla : lsAla[-1] += dicCodon[i]
        elif i in lsArg : lsArg[-1] += dicCodon[i]
        elif i in lsAsn : lsAsn[-1] += dicCodon[i]
        elif i in lsAsp : lsAsp[-1] += dicCodon[i]
        elif i in lsCys : lsCys[-1] += dicCodon[i]
        elif i in lsGln : lsGln[-1] += dicCodon[i]
        elif i in lsGlu : lsGlu[-1] += dicCodon[i]
        elif i in lsGly : lsGly[-1] += dicCodon[i]
        elif i in lsHis : lsHis[-1] += dicCodon[i]
        elif i in lsIle : lsIle[-1] += dicCodon[i]
        elif i in lsLeu : lsLeu[-1] += dicCodon[i]
        elif i in lsLys : lsLys[-1] += dicCodon[i]
        elif i in lsMet : lsMet[-1] += dicCodon[i]
        elif i in lsPhe : lsPhe[-1] += dicCodon[i]
        elif i in lsPro : lsPro[-1] += dicCodon[i]
        elif i in lsSer : lsSer[-1] += dicCodon[i]
        elif i in lsThr : lsThr[-1] += dicCodon[i]
        elif i in lsTrp : lsTrp[-1] += dicCodon[i]
        elif i in lsTyr : lsTyr[-1] += dicCodon[i]
        elif i in lsVal : lsVal[-1] += dicCodon[i]
        elif i in lsStop : lsStop[-1] += dicCodon[i]
    for i in dicCodon :
        if i in lsAla : dicCodon_ratio[i] = dicCodon[i] / lsAla[-1]
        elif i in lsArg : dicCodon_ratio[i] = dicCodon[i] / lsArg[-1]
        elif i in lsAsn : dicCodon_ratio[i] = dicCodon[i] / lsAsn[-1]
        elif i in lsAsp : dicCodon_ratio[i] = dicCodon[i] / lsAsp[-1]
        elif i in lsCys : dicCodon_ratio[i] = dicCodon[i] / lsCys[-1]
        elif i in lsGln : dicCodon_ratio[i] = dicCodon[i] / lsGln[-1]
        elif i in lsGlu : dicCodon_ratio[i] = dicCodon[i] / lsGlu[-1]
        elif i in lsGly : dicCodon_ratio[i] = dicCodon[i] / lsGly[-1]
        elif i in lsHis : dicCodon_ratio[i] = dicCodon[i] / lsHis[-1]
        elif i in lsIle : dicCodon_ratio[i] = dicCodon[i] / lsIle[-1]
        elif i in lsLeu : dicCodon_ratio[i] = dicCodon[i] / lsLeu[-1]
        elif i in lsLys : dicCodon_ratio[i] = dicCodon[i] / lsLys[-1]
        elif i in lsMet : dicCodon_ratio[i] = dicCodon[i] / lsMet[-1]
        elif i in lsPhe : dicCodon_ratio[i] = dicCodon[i] / lsPhe[-1]
        elif i in lsPro : dicCodon_ratio[i] = dicCodon[i] / lsPro[-1]
        elif i in lsSer : dicCodon_ratio[i] = dicCodon[i] / lsSer[-1]
        elif i in lsThr : dicCodon_ratio[i] = dicCodon[i] / lsThr[-1]
        elif i in lsTrp : dicCodon_ratio[i] = dicCodon[i] / lsTrp[-1]
        elif i in lsTyr : dicCodon_ratio[i] = dicCodon[i] / lsTyr[-1]
        elif i in lsVal : dicCodon_ratio[i] = dicCodon[i] / lsVal[-1]
        elif i in lsStop : dicCodon_ratio[i] = dicCodon[i] / lsStop[-1]
    #for check
    print("lsAla: {0}, lsArg: {1}, lsAsn: {2}, lsAsp: {3}, lsCys: {4}, lsGln: {5}, lsGlu: {6}, lsGly: {7}, lsHis: {8}, lsIle: {9}, lsLeu: {10}, lsLys: {11}, lsMet: {12}, lsPhe: {13}, lsPro: {14}, lsSer: {15}, lsThr: {16}, lsTrp: {17}, lsTyr: {18}, lsVal: {19}, lsStop: {20}"
          .format(lsAla, lsArg, lsAsn, lsAsp, lsCys, lsGln, lsGlu, lsGly, lsHis, lsIle, lsLeu, lsLys, lsMet, lsPhe, lsPro, lsSer, lsThr, lsTrp, lsTyr, lsVal, lsStop))
    print("Codon_ratio: ", dicCodon_ratio)

    fWrite = open("D:\\python_output\\Codon_ratio_practice.txt", 'w')
    #write 1 Sequence of the gene, 2 Counted codon, 3 counted codon of the a.a, 4 codon ratio
    fWrite.write( "Read file and the location: {0}\n".format(filename) )
    fWrite.write("Counted codon"), fWrite.write("\n")
    for i in dicCodon :
        fWrite.write(i), fWrite.write(" "), fWrite.write( str( dicCodon[i] ) ), fWrite.write("\n")
    fWrite.write("\n"), fWrite.write("Counted codon of the amino acid\n")
    fWrite.write( "lsAla: {0}\n, lsArg: {1}\n, lsAsn: {2}\n, lsAsp: {3}\n, lsCys: {4}\n, lsGln: {5}\n, lsGlu: {6}\n, lsGly: {7}\n, lsHis: {8}\n, lsIle: {9}\n, lsLeu: {10}\n, lsLys: {11}\n, lsMet: {12}\n, lsPhe: {13}\n, lsPro: {14}\n, lsSer: {15}\n, lsThr: {16}\n, lsTrp: {17}\n, lsTyr: {18}\n, lsVal: {19}\n, lsStop: {20}\n"
          .format(lsAla, lsArg, lsAsn, lsAsp, lsCys, lsGln, lsGlu, lsGly, lsHis, lsIle, lsLeu, lsLys, lsMet, lsPhe, lsPro, lsSer, lsThr, lsTrp, lsTyr, lsVal, lsStop) )
    fWrite.write("\n"), fWrite.write("The codon ratio (a number of a codon / whole counted codon of the a.a)\n")
    for i in dicCodon_ratio :
        fWrite.write(i), fWrite.write(" "), fWrite.write( str( dicCodon_ratio[i] ) ), fWrite.write("\n")
    fWrite.close()
    
main()

