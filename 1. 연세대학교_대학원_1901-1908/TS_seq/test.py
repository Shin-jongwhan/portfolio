#confirm mapping sequence
a = open("C:\\Users\\user\\Desktop\\sequencing\\data\\fasta\\Thellungiella_salsuginea\\GCF_000478725.1_Eutsalg1_0_genomic.fna", 'r')
#c = reference genome
c = a.read().split(">")
del c[0]
for i in range(0, len(c)) : c[i] = c[i].split("\n")
a.close()
for i in range(0, len(c)) :
	c[i][1] = "".join(c[i][1:])
	del c[i][2:]

a = open("C:\\Users\\user\\Desktop\\sequencing\\data\\sam\\TS_genome_and_TS_0mM_miR.trim\\TS_0mM_miR.trim.sam", 'r')
#b = sam file
b = a.read().split("\n")
a.close()
del b[-1]
#del the @ sentence
for i in range(0, len(b)) :
	if "@" in b[i] :
		if "@" not in b[i + 1] :
			del b[:i + 1]
			break
#split [i] by \t
for i in range(0, len(b)) :
	b[i] = b[i].split("\t")


a = open("C:\\Users\\user\\Desktop\\sequencing\\raw_data\\TS\\TS_0mM_miR.trim.fq\\TS_0mM_miR.trim.fq", 'r')
d = a.read().split("\n")
a.close()

##test
#for i in range(0, len(c)) :
#	if b[0].split("\t")[2] == c[i][0] :
#		print(i, c[i][0], c[i][1][ int( b[0].split("\t")[3] ) - 1 : int( b[0].split("\t")[3] ) + int( b[0].split("\t")[5][:-1] ) - 1 ] )
#
#test find multiple mapping in fq
#b[1009] multiple mapping
#>>> b[1009]
#'TCGGACCAGGCTTCATTCCCC'
#>>> for i in range(0, len(c)) :
#	if "TCGGACCAGGCTTCATTCCCC" in c[i][1] :
#		print( i, c[i][1].find("TCGGACCAGGCTTCATTCCCC") )
#
#		
#(32, 2294453)
#(80, 2890741)
#(97, 1329685)
#>>> 
#############################################
##if you wanna get sam flag list, use this
#ls = []
#for i in range(640, len(b)) :
#       if b[i][1] not in ls :
#               ls.append(b[i][1])
