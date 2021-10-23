gff = open("D:\\NGS_data\data\\gff\Thellungiella_salsuginea\\GCF_000478725.1_Eutsalg1_0_genomic.gff", 'r')
lsGff = gff.read().split("\n")
del lsGff[-1]
for i in range(0, len(lsGff)) :
	if "#" in lsGff[i] :
		if "#" not in lsGff[i + 1] :
			del lsGff[:i + 1]
			break

for i in range(len(lsGff) - 1, 0, -1) :
	if "#" in lsGff[i] :
		if "#" not in lsGff[i - 1] and "#" not in lsGff[i - 2] :
			del lsGff[i:]
			break

for i in range(0, len(lsGff)) :
	lsGff[i] = lsGff[i].split("\t")

