Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = open("C:\\Users\\user\\Desktop\\sequencing\\data\\fasta\\Thellungiella_salsuginea\\GCF_000478725.1_Eutsalg1_0_genomic.fna", 'r')

3
>>> c = a.read().split(">")

>>> del c[0]

>>> for i in range(0, len(c)) : c[i] = c[i].split("\n")

>>> a.close()

>>> for i in range(0, len(c)) :
	c[i][1] = "".join(c[i][1:])
	del c[i][2:]

	
>>> a = open("C:\\Users\\user\\Desktop\\sequencing\\data\\sam\\TS_genome_and_TS_0mM_miR.trim\\TS_0mM_miR.trim.sam", 'r')

>>> 
>>> b = a.read().split("\n")

>>> a.close()
>>> del b[-1]

>>> for i in range(0, len(b)) :
	if "@" in b[i] :
		if "@" not in b[i + 1] :
			del b[:i + 1]
			break

		
>>> b[0]
'NS500459:164:HKWHHBGXX:1:11101:19785:1046\t0\tNW_006256877.1\t7339017\t1\t38M\t*\t0\t0\tCCTGTNGGGACCCGAAAGATGGTGAACTATGCCTGAGC\tAAAAA#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\tAS:i:-1\tXS:i:-1\tXN:i:0\tXM:i:1\tXO:i:0\tXG:i:0\tNM:i:1\tMD:Z:5C32\tYT:Z:UU'
>>> b[0].split("\t")[2:4]
['NW_006256877.1', '7339017']
>>> b[0].split("\t")[2:6]
['NW_006256877.1', '7339017', '1', '38M']
>>> len(c)
638
>>> len(c[0])
2
>>> for i in range(0, len(c)) :
	if b[0].split("\t")[2] in c[i][0] :
		print(i, c[i][0])

		
(32, 'NW_006256877.1 Eutrema salsugineum unplaced genomic scaffold, Eutsalg1_0 scaffold_14, whole genome shotgun sequence')
>>> for i in range(0, len(c)) :
	if b[0].split("\t")[2] in c[i][0] :
		print(i, c[i][0], c[i][ int( b[0].split("\t")[3] ) : int( b[0].split("\t")[3] ) + int( b[0].split("\t")[5] ) ] )

		

Traceback (most recent call last):
  File "<pyshell#26>", line 3, in <module>
    print(i, c[i][0], c[i][ int( b[0].split("\t")[3] ) : int( b[0].split("\t")[3] ) + int( b[0].split("\t")[5] ) ] )
ValueError: invalid literal for int() with base 10: '38M'
>>> b[0].split("\t")[5][:-1]
'38'
>>> for i in range(0, len(c)) :
	if b[0].split("\t")[2] in c[i][0] :
		print(i, c[i][0], c[i][ int( b[0].split("\t")[3] ) : int( b[0].split("\t")[3] ) + int( b[0].split("\t")[5][:-1] ) ] )

		
(32, 'NW_006256877.1 Eutrema salsugineum unplaced genomic scaffold, Eutsalg1_0 scaffold_14, whole genome shotgun sequence', [])
>>> for i in range(0, len(c)) :
	if b[0].split("\t")[2] in c[i][0] :
		print(i, c[i][0], c[i][ int( b[0].split("\t")[3] ) : int( b[0].split("\t")[3] ) + int( b[0].split("\t")[5][:-1] ] )
		      
SyntaxError: invalid syntax
>>> for i in range(0, len(c)) :
	if b[0].split("\t")[2] in c[i][0] :
		print(i, c[i][0], c[i][ int( b[0].split("\t")[3] ) : int( b[0].split("\t")[3] ) + int( b[0].split("\t")[5][:-1] ) ] )

		
(32, 'NW_006256877.1 Eutrema salsugineum unplaced genomic scaffold, Eutsalg1_0 scaffold_14, whole genome shotgun sequence', [])
>>> for i in range(0, len(c)) :
	if b[0].split("\t")[2] in c[i][0] :
		print(i, c[i][0], c[i][ int( b[0].split("\t")[3] ) : int( b[0].split("\t")[3] ) + 38 ] )

		
(32, 'NW_006256877.1 Eutrema salsugineum unplaced genomic scaffold, Eutsalg1_0 scaffold_14, whole genome shotgun sequence', [])
>>> for i in range(0, len(c)) :
	if b[0].split("\t")[2] in c[i][0] :
		print(i, c[i][0], c[i][ int( b[0].split("\t")[3] ) ] )

		

Traceback (most recent call last):
  File "<pyshell#36>", line 3, in <module>
    print(i, c[i][0], c[i][ int( b[0].split("\t")[3] ) ] )
IndexError: list index out of range
>>> for i in range(0, len(c)) :
	if b[0].split("\t")[2] in c[i][0] :
		print(i, c[i][0], c[i][1][ int( b[0].split("\t")[3] ) : int( b[0].split("\t")[3] ) + int( b[0].split("\t")[5][:-1] ) ] )

		
(32, 'NW_006256877.1 Eutrema salsugineum unplaced genomic scaffold, Eutsalg1_0 scaffold_14, whole genome shotgun sequence', 'CTGTCGGGACCCGAAAGATGGTGAACTATGCCTGAGCG')
>>> 'NS500459:164:HKWHHBGXX:1:11101:19785:1046\t0\tNW_006256877.1\t7339017\t1\t38M\t*\t0\t0\tCCTGTNGGGACCCGAAAGATGGTGAACTATGCCTGAGC\tAAAAA#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\tAS:i:-1\tXS:i:-1\tXN:i:0\tXM:i:1\tXO:i:0\tXG:i:0\tNM:i:1\tMD:Z:5C32\tYT:Z:UU'
'NS500459:164:HKWHHBGXX:1:11101:19785:1046\t0\tNW_006256877.1\t7339017\t1\t38M\t*\t0\t0\tCCTGTNGGGACCCGAAAGATGGTGAACTATGCCTGAGC\tAAAAA#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\tAS:i:-1\tXS:i:-1\tXN:i:0\tXM:i:1\tXO:i:0\tXG:i:0\tNM:i:1\tMD:Z:5C32\tYT:Z:UU'
>>> 'CTGTCGGGACCCGAAAGATGGTGAACTATGCCTGAGCG'
'CTGTCGGGACCCGAAAGATGGTGAACTATGCCTGAGCG'
>>> CCTGTNGGGACCCGAAAGATGGTGAACTATGCCTGAGC

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    CCTGTNGGGACCCGAAAGATGGTGAACTATGCCTGAGC
NameError: name 'CCTGTNGGGACCCGAAAGATGGTGAACTATGCCTGAGC' is not defined
>>> for i in range(0, len(c)) :
	if b[0].split("\t")[2] in c[i][0] :
		print(i, c[i][0], c[i][1][ int( b[0].split("\t")[3] ) + 1 : int( b[0].split("\t")[3] ) + int( b[0].split("\t")[5][:-1] ) + 1 ] )

		
(32, 'NW_006256877.1 Eutrema salsugineum unplaced genomic scaffold, Eutsalg1_0 scaffold_14, whole genome shotgun sequence', 'TGTCGGGACCCGAAAGATGGTGAACTATGCCTGAGCGG')
>>> 'TGTCGGGACCCGAAAGATGGTGAACTATGCCTGAGCGG'
'TGTCGGGACCCGAAAGATGGTGAACTATGCCTGAGCGG'
>>> for i in range(0, len(c)) :
	if b[0].split("\t")[2] in c[i][0] :
		print(i, c[i][0], c[i][1][ int( b[0].split("\t")[3] ) - 1 : int( b[0].split("\t")[3] ) + int( b[0].split("\t")[5][:-1] ) - 1 ] )

		
(32, 'NW_006256877.1 Eutrema salsugineum unplaced genomic scaffold, Eutsalg1_0 scaffold_14, whole genome shotgun sequence', 'CCTGTCGGGACCCGAAAGATGGTGAACTATGCCTGAGC')
>>> "CCTGTNGGGACCCGAAAGATGGTGAACTATGCCTGAGC"
'CCTGTNGGGACCCGAAAGATGGTGAACTATGCCTGAGC'
>>> 'CCTGTCGGGACCCGAAAGATGGTGAACTATGCCTGAGC'
'CCTGTCGGGACCCGAAAGATGGTGAACTATGCCTGAGC'
>>> len(b)
61534863
>>> 

Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = open("C:\\Users\\user\\Desktop\\sequencing\\raw_data\\TS\\TS_0mM_miR.trim.fq\\TS_0mM_miR.trim.fq", 'r')
>>> b = a.read().split("\n")

>>> len(b)
246139453
>>> len(b) / 2
123069726
>>> b[0:10]
['@NS500459:164:HKWHHBGXX:1:11101:19785:1046 1:N:0:CACCGG', 'CCTGTNGGGACCCGAAAGATGGTGAACTATGCCTGAGC', '+', 'AAAAA#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE', '@NS500459:164:HKWHHBGXX:1:11101:24976:1046 1:N:0:CACCGG', 'TCGGANCAGGCTTCATTCCCC', '+', 'AAAAA#EEEEEEEEEEEEEEA', '@NS500459:164:HKWHHBGXX:1:11101:14758:1046 1:N:0:CACCGG', 'TGTATNCAGCTGAGGCATCCTAACAGACCGGTAGACTTGAAC']
>>> len(b) / 4
61534863
>>> 
