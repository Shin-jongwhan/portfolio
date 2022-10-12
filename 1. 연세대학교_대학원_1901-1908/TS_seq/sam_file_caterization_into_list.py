## 1st
## sorting sam file into list by fragment
## [3] = annotation start position, [5] = the number of the nt [9] = fragment sequence
def main() :
    fSam = open("D:\\NGS_data\\UNIST\\data\\sam\\Fur_Fe_1_ChIP.sam", 'r')
    lsSam = fSam.read().split("\n")
    fSam.close()
    for i in range(0, len(lsSam)) :
        lsSam[i] = lsSam[i].split("\t")
    del lsSam[-1]

    #sorting by sequence
    intSam_start = 0
    for i in range(0, len(b)) :
	if "@" in b[i] :
		if "@" not in b[i + 1] :
			print("read start position : ", i + 1)
			intSam_start = i + 1
			break
    lsSam[intSam_start:] = sorted(lsSam[intSam_start:], key = lambda element:element[9])
    
    print( "The number of reads in the sam file : ", len(lsSam[intSam_start:]) )
    fWrite = open("C:\\Users\\Shin\\Desktop\\과제\\TS_miRNA_seq_2\\breakthrough\\sam_sort_test.txt", 'w')
    for i in range(0, len(lsSam)) :
        fWrite.write( "\t".join(lsSam[i]) )
        fWrite.write("\n")
    fWrite.close()
    return lsSam

lsSam = main()
lsSam
