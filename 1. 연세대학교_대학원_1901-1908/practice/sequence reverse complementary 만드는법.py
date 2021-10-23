Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = "TTTTTCTAAATGATTATCCACTGAAGTGTTTGGGGGAACTCCCGGACCCATTCAACGGATT"
>>> a[:-1]
'TTTTTCTAAATGATTATCCACTGAAGTGTTTGGGGGAACTCCCGGACCCATTCAACGGAT'
>>> a[::-1]
'TTAGGCAACTTACCCAGGCCCTCAAGGGGGTTTGTGAAGTCACCTATTAGTAAATCTTTTT'
>>> Complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}
>>> b = "".join([ Complement.get(base, '') for base in a[::-1] ])
>>> b
'AATCCGTTGAATGGGTCCGGGAGTTCCCCCAAACACTTCAGTGGATAATCATTTAGAAAAA'
>>> b
'AATCCGTTGAATGGGTCCGGGAGTTCCCCCAAACACTTCAGTGGATAATCATTTAGAAAAA'
>>> a = ">microRNA_ath-miR395b[NC_003070.9;9364519:9364580;+]
ACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG
>microRNA_ath-miR395c[NC_003070.9;9367128:9367189;+]
ACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG
>microRNA_ath-miR395d[NC_003070.9;26269968:26270029;-]
TAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC
>microRNA_ath-miR395e[NC_003070.9;26272765:26272826;-]
ttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT
>microRNA_ath-miR395f[NC_003070.9;26273918:26273979;+]
ATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC"
SyntaxError: EOL while scanning string literal
>>> a = ">microRNA_ath-miR395b[NC_003070.9;9364519:9364580;+]\nACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG\n>microRNA_ath-miR395c[NC_003070.9;9367128:9367189;+]\nACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG\n>microRNA_ath-miR395d[NC_003070.9;26269968:26270029;-]\nTAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC\n>microRNA_ath-miR395e[NC_003070.9;26272765:26272826;-]\nttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT\n>microRNA_ath-miR395f[NC_003070.9;26273918:26273979;+]\nATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC"
>>> a
'>microRNA_ath-miR395b[NC_003070.9;9364519:9364580;+]\nACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG\n>microRNA_ath-miR395c[NC_003070.9;9367128:9367189;+]\nACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG\n>microRNA_ath-miR395d[NC_003070.9;26269968:26270029;-]\nTAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC\n>microRNA_ath-miR395e[NC_003070.9;26272765:26272826;-]\nttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT\n>microRNA_ath-miR395f[NC_003070.9;26273918:26273979;+]\nATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC'
>>> a.split("\n")
['>microRNA_ath-miR395b[NC_003070.9;9364519:9364580;+]', 'ACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG', '>microRNA_ath-miR395c[NC_003070.9;9367128:9367189;+]', 'ACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG', '>microRNA_ath-miR395d[NC_003070.9;26269968:26270029;-]', 'TAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC', '>microRNA_ath-miR395e[NC_003070.9;26272765:26272826;-]', 'ttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT', '>microRNA_ath-miR395f[NC_003070.9;26273918:26273979;+]', 'ATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC']
>>> a[0]
'>'
>>> a[1]
'm'
>>> a(1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a(1)
TypeError: 'str' object is not callable
>>> a
'>microRNA_ath-miR395b[NC_003070.9;9364519:9364580;+]\nACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG\n>microRNA_ath-miR395c[NC_003070.9;9367128:9367189;+]\nACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG\n>microRNA_ath-miR395d[NC_003070.9;26269968:26270029;-]\nTAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC\n>microRNA_ath-miR395e[NC_003070.9;26272765:26272826;-]\nttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT\n>microRNA_ath-miR395f[NC_003070.9;26273918:26273979;+]\nATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC'
>>> a = a.split("\n")
>>> a
['>microRNA_ath-miR395b[NC_003070.9;9364519:9364580;+]', 'ACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG', '>microRNA_ath-miR395c[NC_003070.9;9367128:9367189;+]', 'ACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG', '>microRNA_ath-miR395d[NC_003070.9;26269968:26270029;-]', 'TAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC', '>microRNA_ath-miR395e[NC_003070.9;26272765:26272826;-]', 'ttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT', '>microRNA_ath-miR395f[NC_003070.9;26273918:26273979;+]', 'ATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC']
>>> a[0]
'>microRNA_ath-miR395b[NC_003070.9;9364519:9364580;+]'
>>> del a[0]
>>> a
['ACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG', '>microRNA_ath-miR395c[NC_003070.9;9367128:9367189;+]', 'ACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG', '>microRNA_ath-miR395d[NC_003070.9;26269968:26270029;-]', 'TAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC', '>microRNA_ath-miR395e[NC_003070.9;26272765:26272826;-]', 'ttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT', '>microRNA_ath-miR395f[NC_003070.9;26273918:26273979;+]', 'ATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC']
>>> for i in a :
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> for i in a :
	print(i)

	
ACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG
>microRNA_ath-miR395c[NC_003070.9;9367128:9367189;+]
ACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG
>microRNA_ath-miR395d[NC_003070.9;26269968:26270029;-]
TAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC
>microRNA_ath-miR395e[NC_003070.9;26272765:26272826;-]
ttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT
>microRNA_ath-miR395f[NC_003070.9;26273918:26273979;+]
ATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC
>>> len(a)
9
>>> for i in len(a) :
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    for i in len(a) :
TypeError: 'int' object is not iterable
>>> for i in range(0, len(a)) :
	print(i)

	
0
1
2
3
4
5
6
7
8
>>> for i in range(0, len(a)) :
	if ">" in a[-i] :
		printa[-i]

		
Traceback (most recent call last):
  File "<pyshell#38>", line 3, in <module>
    printa[-i]
NameError: name 'printa' is not defined
>>> for i in range(0, len(a)) :
	if ">" in a[-i] :
		print[-i]

		
Traceback (most recent call last):
  File "<pyshell#40>", line 3, in <module>
    print[-i]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> for i in range(0, len(a)) :
	if ">" in a[-i] :
		print(a[-i])

		
>microRNA_ath-miR395f[NC_003070.9;26273918:26273979;+]
>microRNA_ath-miR395e[NC_003070.9;26272765:26272826;-]
>microRNA_ath-miR395d[NC_003070.9;26269968:26270029;-]
>microRNA_ath-miR395c[NC_003070.9;9367128:9367189;+]
>>> for i in range(0, len(a)) :
	if ">" in a[-i] :
		del a[-i]

		
Traceback (most recent call last):
  File "<pyshell#44>", line 2, in <module>
    if ">" in a[-i] :
IndexError: list index out of range
>>> a
['ACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG', 'ACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG', 'TAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC', 'ttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT', 'ATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC']
>>> Complement
{'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
>>> b = "".join([ Complement.get(base, '') for base in a[::-1] ])
>>> b
''
>>> a
['ACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG', 'ACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG', 'TAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC', 'ttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT', 'ATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC']
>>> b = []
>>> b = "".join([ Complement.get(base, '') for base in a[for i in range(0, len(a))[::-1] ])
		
SyntaxError: invalid syntax
>>> 
		
>>> b = "".join([ Complement.get(base, '') for base in a[for i in range(0, len(a))][::-1] ])
		
SyntaxError: invalid syntax
>>> for i in range(0, len(a)) :
		b[i] = "".join([ Complement.get(base, '') for base in a[i][::-1] ])

		
Traceback (most recent call last):
  File "<pyshell#56>", line 2, in <module>
    b[i] = "".join([ Complement.get(base, '') for base in a[i][::-1] ])
IndexError: list assignment index out of range
>>> b
		
[]
>>> b[0]
		
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    b[0]
IndexError: list index out of range
>>> b[0] = 1
		
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    b[0] = 1
IndexError: list assignment index out of range
>>> b.append[1]
		
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    b.append[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> b.append["1"]
		
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    b.append["1"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> b.append("1")
		
>>> b
		
['1']
>>> b = []
		
>>> for i in range(0, len(a)) :
		b.append( "".join([ Complement.get(base, '') for base in a[i][::-1] ]) )

		
>>> b
		
['CTACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTGTATACAAACCAATGT', 'CAACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTATATACAAACCAATGT', 'GCATCACCAAATGACATCGGGAGTTCCCCCAAACACTTCAGTGGAATTAACTGTTAGCTTA', 'AAAATACCGAATCAGCCCGGGAGTTCCCCCAAACACTTCAG', 'GGGTGCCAAGATGTCACCTAGAGTCCCCCCAAACACTTCAGTGTTCATCAGATTGATTGAT']
>>> for i in b : print(i)

		
CTACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTGTATACAAACCAATGT
CAACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTATATACAAACCAATGT
GCATCACCAAATGACATCGGGAGTTCCCCCAAACACTTCAGTGGAATTAACTGTTAGCTTA
AAAATACCGAATCAGCCCGGGAGTTCCCCCAAACACTTCAG
GGGTGCCAAGATGTCACCTAGAGTCCCCCCAAACACTTCAGTGTTCATCAGATTGATTGAT
>>> a = ">microRNA_ath-miR395b[NC_003070.9;9364519:9364580;+]\nACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG\n>microRNA_ath-miR395c[NC_003070.9;9367128:9367189;+]\nACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG\n>microRNA_ath-miR395d[NC_003070.9;26269968:26270029;-]\nTAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC\n>microRNA_ath-miR395e[NC_003070.9;26272765:26272826;-]\nttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT\n>microRNA_ath-miR395f[NC_003070.9;26273918:26273979;+]\nATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC"
		
>>> a = a.split("\n")
		
>>> a[0]
		
'>microRNA_ath-miR395b[NC_003070.9;9364519:9364580;+]'
>>> for i in range(0, len(a)) :
	if ">" in a[-i] :
		del a[-i]

		
Traceback (most recent call last):
  File "<pyshell#74>", line 2, in <module>
    if ">" in a[-i] :
IndexError: list index out of range
>>> a
		
['ACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG', 'ACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG', 'TAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC', 'ttttataaaatagttttctaCTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT', 'ATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC']
>>> b = []
		
>>> for i in range(0, len(a)) :
		b.append( "".join([ Complement.get(base, '') for base in a[i][::-1] ]) )

		
>>> b
		
['CTACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTGTATACAAACCAATGT', 'CAACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTATATACAAACCAATGT', 'GCATCACCAAATGACATCGGGAGTTCCCCCAAACACTTCAGTGGAATTAACTGTTAGCTTA', 'AAAATACCGAATCAGCCCGGGAGTTCCCCCAAACACTTCAG', 'GGGTGCCAAGATGTCACCTAGAGTCCCCCCAAACACTTCAGTGTTCATCAGATTGATTGAT']
>>> for i in range(0, len(a)) :
		a[i] = a[i].upper()

		
>>> a
		
['ACATTGGTTTGTATACAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTAG', 'ACATTGGTTTGTATATAACACTGAAGTGTTTGGGGGGACTCTTGGTGTCATTCTGGCGTTG', 'TAAGCTAACAGTTAATTCCACTGAAGTGTTTGGGGGAACTCCCGATGTCATTTGGTGATGC', 'TTTTATAAAATAGTTTTCTACTGAAGTGTTTGGGGGAACTCCCGGGCTGATTCGGTATTTT', 'ATCAATCAATCTGATGAACACTGAAGTGTTTGGGGGGACTCTAGGTGACATCTTGGCACCC']
>>> for i in range(0, len(a)) :
		b.append( "".join([ Complement.get(base, '') for base in a[i][::-1] ]) )

		
>>> b
		
['CTACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTGTATACAAACCAATGT', 'CAACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTATATACAAACCAATGT', 'GCATCACCAAATGACATCGGGAGTTCCCCCAAACACTTCAGTGGAATTAACTGTTAGCTTA', 'AAAATACCGAATCAGCCCGGGAGTTCCCCCAAACACTTCAG', 'GGGTGCCAAGATGTCACCTAGAGTCCCCCCAAACACTTCAGTGTTCATCAGATTGATTGAT', 'CTACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTGTATACAAACCAATGT', 'CAACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTATATACAAACCAATGT', 'GCATCACCAAATGACATCGGGAGTTCCCCCAAACACTTCAGTGGAATTAACTGTTAGCTTA', 'AAAATACCGAATCAGCCCGGGAGTTCCCCCAAACACTTCAGTAGAAAACTATTTTATAAAA', 'GGGTGCCAAGATGTCACCTAGAGTCCCCCCAAACACTTCAGTGTTCATCAGATTGATTGAT']
>>> b = []
		
>>> for i in range(0, len(a)) :
		b.append( "".join([ Complement.get(base, '') for base in a[i][::-1] ]) )

		
>>> b
		
['CTACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTGTATACAAACCAATGT', 'CAACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTATATACAAACCAATGT', 'GCATCACCAAATGACATCGGGAGTTCCCCCAAACACTTCAGTGGAATTAACTGTTAGCTTA', 'AAAATACCGAATCAGCCCGGGAGTTCCCCCAAACACTTCAGTAGAAAACTATTTTATAAAA', 'GGGTGCCAAGATGTCACCTAGAGTCCCCCCAAACACTTCAGTGTTCATCAGATTGATTGAT']
>>> for i in b : print(i)

		
CTACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTGTATACAAACCAATGT
CAACGCCAGAATGACACCAAGAGTCCCCCCAAACACTTCAGTGTTATATACAAACCAATGT
GCATCACCAAATGACATCGGGAGTTCCCCCAAACACTTCAGTGGAATTAACTGTTAGCTTA
AAAATACCGAATCAGCCCGGGAGTTCCCCCAAACACTTCAGTAGAAAACTATTTTATAAAA
GGGTGCCAAGATGTCACCTAGAGTCCCCCCAAACACTTCAGTGTTCATCAGATTGATTGAT
>>> 
>>> Complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}
>>> for i in range(0, len(a)) :
		b.append( "".join([ Complement.get(base, '') for base in a[i][::-1] ]) )
### b의 리스트에 append 해서 넣는 법
>>> b = "".join([ Complement.get(base, '') for base in a[::-1] ])
### b를 그냥 reverse complementary로 만드는 법 
