#-*- coding:utf-8 -*-

def backup_num_1() :
    fRead = open("C:\\Users\\user\\Desktop\\업무\\일일\\앙팡가드\\과제\\200629_백업관련\\2. Backup_bros_EnfantGuard_1607-1612_180411.txt", 'r')
    fResult = open("C:\\Users\\user\\Desktop\\업무\\일일\\앙팡가드\\과제\\200629_백업관련\\2. Backup_bros_EnfantGuard_1607-1612_180411_parsing.txt", 'w')

    lsRead = fRead.readlines()

    fRead.close()

    lsResult = []
    sample_tmp = ""
    for i in range(0, len(lsRead)) :
        lsRead[i] = lsRead[i].strip()
        if "├" in lsRead[i] and "." not in lsRead[i] and ("NS500759" in lsRead[i] or "NS500435" in lsRead[i] or "NB501509" in lsRead[i] or "NDX550181" in lsRead[i]) :
            run_id = lsRead[i].split("─")[1]
            print(lsRead[i])

        if "─" in lsRead[i] and "-" in lsRead[i] :
            if len(lsRead[i].split("─")[1].split("-")[0]) == 13 :
                sample = lsRead[i].split("─")[1]
                sample_id = lsRead[i].split("─")[1].split("-")[0]
                if sample_tmp == "" :
                    sample_tmp = sample
                if sample_tmp == sample :
                    continue
                elif sample_tmp != sample :
                    sample_tmp = sample
                if "." not in lsRead[i] and "_" not in lsRead[i] and len(sample_id) == 13 :
                    #print(lsRead[i])
                    lsResult.append([ run_id, sample ])
                    if " " not in lsRead[i] :
                        print("etc", lsRead[i])
                        lsResult.append( [ "etc", sample ] )
                    #print(lsResult[-1])
                    fResult.write("\t".join(lsResult[-1]) + "\n")

    fResult.close()


def backup_num_2() :
    fRead = open("C:\\Users\\user\\Desktop\\업무\\일일\\앙팡가드\\과제\\200629_백업관련\\8. Backup_bros_EnfantGuard_1908-1912_200820.txt", 'r', encoding = 'utf-8')
    fResult = open("C:\\Users\\user\\Desktop\\업무\\일일\\앙팡가드\\과제\\200629_백업관련\\8. Backup_bros_EnfantGuard_1908-1912_200820_parsing.txt", 'w')

    lsRead = fRead.readlines()

    #lsRead = []
    #while True :
    #    print(type(fRead.readline()))
    #    i = (fRead.readline()).decode('cp949').encode('utf-8')
    #    if i != "" : 
    #        lsRead.append(i)
    #    else :
    #        break

    fRead.close()

    lsResult = []
    sample_tmp = ""
    for i in range(0, len(lsRead)) :
        lsRead[i] = lsRead[i].strip()
        if "@" in lsRead[i] :
            sample = lsRead[i].split(" ")[-1].split("@")[0]
            run_id = lsRead[i].split("@")[1].split(".")[0]
            #print(run_id, sample)
            fResult.write( run_id + "\t" + sample + "\n")

    fResult.close()


def main() :
    backup_num_2()


main()
