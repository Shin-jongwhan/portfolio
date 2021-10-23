a = open("D:\\NGS_data\\data\\fasta\\arabidopsis_thaliana\\arabidopsis_thaliana_mature_miRNA.pl_replace_U.fasta", 'r')
b = open("D:\\NGS_data\\data\\fasta\\arabidopsis_thaliana\\arabidopsis_thaliana_pri_miRNA.pl_replace_U.fasta", 'r')
lsMature = []
lsMature = a.read().split("\n")
lsPri = []
lsPri = b.read().split("\n")
a.close()
b.close()
del lsMature[-1]
del lsPri[-1]
c = []
for i in range(0, len(lsMature)) :
	for k in range(0, len(lsPri)) :
		if lsPri[k][1:lsPri[k].find(" ")].upper() in lsMature[i][1:lsMature[i].find(" ")].upper() :
			c.append( [ lsMature[i][1:lsMature[i].find(" ")] ] )
			c[-1].append( lsPri[k+1][ lsPri[k+1].find(lsMature[i+1]) - 20 : lsPri[k+1].find(lsMature[i+1]) ] + " " + lsPri[k+1][ lsPri[k+1].find(lsMature[i+1]) : lsPri[k+1].find(lsMature[i+1]) + len(lsMature[i+1]) ] + " " + lsPri[k+1][ lsPri[k+1].find(lsMature[i+1]) + len(lsMature[i+1]) : lsPri[k+1].find(lsMature[i+1]) + len(lsMature[i+1]) + 20 ] )

#for i in range(0, len(c)) :
#    print(c[i][1])

for i in range(0, len(c)) :
    c[i][1] = c[i][1].split(" ")
    #print(c[i][1])


dicMotif_2 = {}
sNuc = "ACGT"
for i in sNuc :
    for k in sNuc :
        dicMotif_2[i+k] = 0
dicMotif_2_1 = dicMotif_2
print(dicMotif_2)

dicMotif_1 = {}
for i in sNuc :
    dicMotif_1[i] = 0

for i in range(0, len(c)) :
    for k in range(0, len(dicMotif_2)) :
        if list(dicMotif_2.keys())[k] == c[i][1][0][-2 : ] :
            dicMotif_2[list(dicMotif_2.keys())[k]] += 1
print(dicMotif_2)

for i in range(0, len(c)) :
    for k in range(0, len(dicMotif_1)) :
        if list(dicMotif_1.keys())[k] == c[i][1][0][-15:-14] :
            dicMotif_1[list(dicMotif_1.keys())[k]] += 1
print(dicMotif_1)

for i in range(0, len(c)) :
    for k in range(0, len(dicMotif_2_1)) :
        for j in range(0, len(c[i][1][1])) :
            if list(dicMotif_2_1.keys())[k] == c[i][1][1][j : j + 2] :
                dicMotif_2_1[list(dicMotif_2_1.keys())[k]] += 1
print(dicMotif_2_1)
