#[0] = chromosome 1, [4] = chromosome 5, [5] = mitochondrion, [6] = chloroplast
# gff3 파일과 anootation 맞추려면 [a -1, b] 해야함 
a = open("D:\\NGS_data\\data\\fasta\\arabidopsis_thaliana\\GCF_000001735.4_TAIR10.1_genomic.fna", 'r')
b = a.read()
a.close()
b = b.split(">")[1:]
print(len(b))
for i in range(0, len(b)) :
	b[i] = ''.join(b[i].split("\n")[1:])    #시퀀스만 얻어낸 것
print(len(b))

#for i in range(0, len(b)) :
#	b[i] = b[i].upper()
#ex) b[3][5723651 - 1:5727268] = CRY1의 full lenth genomic
#ex) b[3][5724260-1:5724593] = CRY1의 첫번째 CDS
