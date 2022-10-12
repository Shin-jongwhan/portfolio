a = open("D:\\NGS_data\\data\\fasta\\arabidopsis_thaliana\\arabidopsis_thaliana_pri_miRNA.pl.fasta", 'r')
b = a.read().split("\n")
print(b[0])
print(b[-1])
a.close()

for i in range(1, len(b), 2) :
    b[i] = b[i].replace("U", "T")

f = open("D:\\NGS_data\\data\\fasta\\arabidopsis_thaliana\\arabidopsis_thaliana_pri_miRNA.pl_replace_U.fasta", 'w')
for i in range(0, len(b)) :
    f.write(b[i])
    f.write("\n")

f.close()
