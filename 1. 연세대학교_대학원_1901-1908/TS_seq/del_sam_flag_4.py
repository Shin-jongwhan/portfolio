# 2nd
a = open("C:\\Users\\Shin\\Desktop\\과제\\TS_miRNA_seq_2\\breakthrough\\sam_sort_test_fur_fe_1_chip.txt", 'r')
b = a.read().split("\n")
a.close()
Sam_start = 0
for i in range(0, len(b)) :
	if "@" in b[i] :
		if "@" not in b[i + 1] :
			print("read start position : ", i + 1)
			Sam_start = i + 1
			break
print("total number of reads : ", len(b[3:]))
del b[-1]

for i in range(0, len(b)) :
	b[i] = b[i].split("\t")

#sort by sam flag
b[3:] = sorted(b[3:], key = lambda element:element[1])
ls = []
for i in range(len(b) - 1, 2, -1) :
	if b[i][1] == "4" :
		ls.append(i)
		del b[i]

print( "the numeber of sam flag 4 : ", len(ls) )
fWrite = open("C:\\Users\\Shin\\Desktop\\과제\\TS_miRNA_seq_2\\breakthrough\\del_flag_4_test_fur_fe_1_chip.txt", 'w')
for i in range(0, len(b)) :
	fWrite.write("\t".join(b[i]))
	fWrite.write("\n")
fWrite.close()
