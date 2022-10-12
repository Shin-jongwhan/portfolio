a = open("D:\\NGS_data\\data\\sam\\AT_mature_miR_ref_TS_0mM_miR.trim\\AT_mature_miR_ref_TS_0mM_miR.trim.sam", 'r')
b = []

def readline(a, b) :
        print("readline 100000000")
        for i in range(0, 100000000) :
                readline = a.readline()
                if readline == '' :
                        break
                if "@" in readline :
                        continue
                if readline.split("\t")[1] == "4" :
                        continue
                if readline.split("\t")[1] != "4" :
                        b.append(readline)

readline(a, b)
#readline(a, b)
#readline(a, b)
#readline(a, b)
#readline(a, b)
#readline(a, b)
#readline(a, b)
#readline(a, b)
#readline(a, b)
#readline(a, b)
print("readline done")
a.close()

print("write file")
f = open("C:\\Users\\Shin\\Desktop\\과제\\TS_miRNA_seq_2\\breakthrough\\test.txt", 'w')
for i in range(0, len(b)) :
	f.write(b[i])
f.close()
