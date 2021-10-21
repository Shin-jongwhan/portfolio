def count_sample() :
    sPlot_input = open("C:\\Users\\user\\Desktop\\업무\\과제\\앙팡가드\\1.개발자료\\최종output_201008\\all\\200kb_del_400Kb_dup_test\\Plot_input.txt", 'r')
    lsPlot_input = []
    lsPlot_input_header = sPlot_input.readline().strip().split("\t")

    for i in sPlot_input :
        lsPlot_input.append(i.strip().split("\t"))

    print("Number of Plot_input : {0}".format(len(lsPlot_input)))
    #print(lsPlot_input[0])
    #print(lsPlot_input[-1])
    #print(lsPlot_input_header)
    
    sPlot_input.close()

    lsPlot_input.sort(key = lambda x : x[4])
    #print(lsPlot_input[0])
    #print(lsPlot_input[-1])

    nCount_sample = 0
    sSample_tmp = ""
    for i in range(0, len(lsPlot_input)) :
        if sSample_tmp == "" :
            sSample_tmp = lsPlot_input[i][4]
            nCount_sample += 1
        elif sSample_tmp == lsPlot_input[i][4] :
            continue
        elif sSample_tmp != lsPlot_input[i][4] :
            sSample_tmp = lsPlot_input[i][4]
            nCount_sample += 1

    print("Counted num of sample : {0}".format(nCount_sample))


def main() :
    count_sample()


main()
