


# application, how to find contig start and end position
#>>> a
#[[1, 2], [3, 4], [1, 5]]
#>>> sContig_S = 0
#>>> sContig_E = 0
#>>> for i in range(0, len(a)) :
#	print("i : ", i)
#	if a[i][0] == 1 :
#		sContig_S = i
#		for k in range(len(a) - 1, -1, -1) :
#			print("k : ", k)
#			if a[k][0] == 1 :
#				sContig_E = k + 1
#				print(sContig_S, sContig_E)
#				break
#		break
#
#	
#i :  0
#k :  2
#0 3
