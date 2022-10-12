# 3rd
# counting the identical fragment
a = open("C:\\Users\\Shin\\Desktop\\과제\\TS_miRNA_seq_2\\breakthrough\\del_flag_4_test_fur_fe_1_chip.txt", 'r')
b = a.read().split("\n")
a.close()
del b[-1]
intSam_start = 0
for i in range(0, len(b)) :
	if "@" in b[i] :
		if "@" not in b[i + 1] :
			print("read start position : ", i + 1)
			intSam_start = i + 1
			break
for i in range(0, len(b)) :
    b[i] = b[i].split("\t")

print(b[0])
print("how many reads exist in sam file except for sam flag 4 : ", len(b))

#sort each identical seq as annotation location
lsSort_range = [ intSam_start, (intSam_start + 1) ]           #initialization
for i in range(intSam_start, len(b) - 1) :
        if b[i][9] == b[i + 1][9] :
                lsSort_range[1] = i + 2
                continue
        elif b[i][9] != b[i + 1][9] :
                b[ lsSort_range[0] : lsSort_range[1] ] = sorted(b[ lsSort_range[0] : lsSort_range[1] ], key = lambda element:element[3])
                lsSort_range = [ (i + 1), (i + 2) ]

lsCountSeq = []
for i in range(intSam_start, len(b) - 1) :
    if i == intSam_start :
        lsCountSeq.append(b[i])
        lsCountSeq[-1].append(1)
        continue
    elif i > intSam_start :
        if b[i][9] == b[i + 1][9] :
                if b[i][3] == b[i + 1][3] :
                        lsCountSeq[-1][-1] += 1
                        continue
                elif b[i][3] != b[i + 1][3] :
                        lsCountSeq.append(b[i + 1])
                        lsCountSeq[-1].append(1)
                        continue
        elif b[i][9] != b[i + 1][9] :
                lsCountSeq.append(b[i + 1])
                lsCountSeq[-1].append(1)


lsCountSeq = sorted(lsCountSeq, key = lambda element:element[-1])
for i in range(0, len(lsCountSeq)) :
    lsCountSeq[i][-1] = str(lsCountSeq[i][-1])
print("the number of counted seq : ", len(lsCountSeq))
print("biggest counted identical reads and how many times it counted : ", lsCountSeq[-1][9], lsCountSeq[-1][-1])

fWrite = open("C:\\Users\\Shin\\Desktop\\과제\\TS_miRNA_seq_2\\breakthrough\\fur_fe_1_chip_count_identical.txt", 'w')
for i in range(0, intSam_start) :
    if i < (intSam_start - 1) : 
        fWrite.write("\t".join( b[i] ))
        fWrite.write("\n")
    elif i == (intSam_start - 1) :
        fWrite.write("\t".join( b[i] ))
for i in range(0, len(lsCountSeq)) :
    fWrite.write("\t".join( lsCountSeq[i] ))
    fWrite.write("\n")

fWrite.close()
