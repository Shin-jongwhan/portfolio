#NS500459:508:HMMT7BGX9:1:11101:12400:1055	0	KZ772775.1	111888	42	20M	*	0	0	TTCGGNCCAGGCTTCATTCC
#AAAAA#EEEEEEEEEEEEEE	AS:i:-1	XN:i:0	XM:i:1	XO:i:0	XG:i:0	NM:i:1	MD:Z:5A14	YT:Z:UU
## [1] sam flag [2] chromosome / contigue [3] start position [9] sequence
###
##gff-version 3
#!gff-spec-version 1.21
#!processor NCBI annotwriter
#!genome-build Marchanta_polymorpha_v1
#!genome-build-accession NCBI_Assembly:GCA_003032435.1
##sequence-region KZ772944.1 1 3475129
##species https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3197
#KZ772944.1	Genbank	region	1	3475129	.	+	.
#ID=id0;Dbxref=taxon:3197;Name=Y;chromosome=Y;gbkey=Src;genome=genomic;map=unlocalized;mol_type=genomic DNA;strain=Tak-1
## [0] contigue [2] region, gene, mRNA, exon, CDS... [3] SS [4] ES [6] strand
def main() :
    sSam_dir = "D:\\NGS_data\\data\\sam\\PhD_jung_hyunju\\marchantia\\my_trimming_data\\Mpo_genome_ref_Mpo_0h_drought_trim\\Mpo_genome_ref_Mpo_0h_trim_del_samF_4.sam"
    sGff_dir = "D:\\NGS_data\\data\\gff\\Marchantia_polymorpha\\GCA_003032435.1_Mp_v1_tak1_genomic.gff"
    fSam = open(sSam_dir, 'r')
    fGff = open(sGff_dir, 'r')
    lsMIR_candi = []
    lsGff_gene = []
    nAlign_S = 0
    lsGff = []
    while True :
        i = fGff.readline()
        if "#" in i :
            continue
        else : 
            lsGff.append(i.split("\t"))
        if "" == i :
            break
    del lsGff[-1]

    for i in range(0, len(lsGff)) :
        if lsGff[i][2] == "gene" :
            lsGff_gene.append(lsGff[i])
    print(len(lsGff_gene))
    ## sam : [1] sam flag [2] chromosome / contigue [3] start position [9] sequence
    ## gff : [0] contigue [2] region, gene, mRNA, exon, CDS... [3] SS [4] ES [6] strand
    #while True :
    #    i = fSam.readline()
    #    if "@" in i :
    #        k = fSam.readline()
    #        if "@" not in k :
    #            for j in range(0, len(lsGff)) :
    #                if int(lsGff[j][3]) <=
    #            break

    
    fSam.close()
    fGff.close()

main()
