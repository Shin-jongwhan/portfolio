# This function is to choose specific gene sequence
# of a species in hairpin, mature miRNA fasta file from mirbase
def main() :
    fRead = open("D:\\NGS_data\\data\\fasta\\hairpin.fa", 'r')
    lsFasta = []
    lsPar_species = []
    lsFasta = fRead.read().split(">")
    fRead.close()
    for i in range(0, len(lsFasta)) :
        if "Arabidopsis thaliana" in lsFasta[i].split("\n")[0] :
            lsPar_species.append(lsFasta[i])

    fWrite = open("D:\\NGS_data\\data\\fasta\\AT_hairpin.fa", 'w')
    for i in range(0, len(lsPar_species)) :
        fWrite.write(">")
        fWrite.write(lsPar_species[i])
    fWrite.close()

main()
