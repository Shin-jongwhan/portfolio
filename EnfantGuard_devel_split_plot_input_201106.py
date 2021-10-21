import os
import time


def Plot_input_split(fPlot_input, nSplitter_num, lsMkdir) : 
        lsPlot_input = []
        lsPlot_input_header = []

        lsPlot_input_header = fPlot_input.readline().strip().split("\t")
        
        for i in fPlot_input : 
                lsPlot_input.append( i.strip().split("\t") )
        
        for i in range(0, len(lsMkdir)) : 
                fPlot_input_split = open("{0}/Plot_input.txt".format(lsMkdir[i]), "w")
                fPlot_input_split.write("\t".join(lsPlot_input_header) + "\n")
                if i == 0 : 
                        for j in range(0, int(len(lsPlot_input) / nSplitter_num)) : 
                                fPlot_input_split.write("\t".join(lsPlot_input[j]) + "\n")
                else : 
                        for j in range(int( (len(lsPlot_input) / nSplitter_num) * i ), int( (len(lsPlot_input) / nSplitter_num) * (i + 1) ) ) : 
                                fPlot_input_split.write("\t".join(lsPlot_input[j]) + "\n")
                fPlot_input_split.close()



def get_split_dir(nSplitter_num) : 
        lsMkdir = []

        for i in range(1, nSplitter_num + 1) : 
                lsMkdir.append("split{0}".format(i))

        for i in range(0, len(lsMkdir)) : 
                if lsMkdir[i] in os.listdir("./") : 
                        print("{0} directory is aleady exist. Progress deleting directory.".format(lsMkdir[i]))
                        os.system("rm -rf {0}".format(lsMkdir[i]))
                        time.sleep(0.5)
                os.system("mkdir {0}".format(lsMkdir[i]))

        return lsMkdir


def get_split_plot(sPlot_input_dir, lsMkdir) : 
        for i in range(0, len(lsMkdir)) : 
                os.chdir(sPlot_input_dir + lsMkdir[i])
                os.system("python /data/Analysis/ETC/enfant_call_test_171228/Script/woo_scripts/11.plot_split.1M.dupdel.py Plot_input.txt")
                os.system("/data/Analysis/ETC/enfant_call_test_171228/Script/woo_scripts/enfant_sub_plot2_Scatter_v2_1M_del.R")
                os.system("/data/Analysis/ETC/enfant_call_test_171228/Script/woo_scripts/enfant_sub_plot2_Scatter_v2_1M_dup.R")
                



def main() : 
        sPlot_input_dir1 = "/data/Analysis/ETC/enfant_call_test_171228/3.Run/Confirm_sample_list_JH_200831_1/200kb_del_400Kb_dup_test/"
        sPlot_input_dir2 = "/data/Analysis/ETC/enfant_call_test_171228/3.Run/Confirm_sample_list_JH_200831_2/200kb_del_400Kb_dup_test/"
        sPlot_input_dir3 = "/data/Analysis/ETC/enfant_call_test_171228/3.Run/Confirm_sample_list_JH_200831_3/200kb_del_400Kb_dup_test/"
        
        nSplitter_num = 4
        
        os.chdir(sPlot_input_dir1)
        lsMkdir = get_split_dir(nSplitter_num)
        fPlot_input1 = open("Plot_input.txt", 'r')
        Plot_input_split(fPlot_input1, nSplitter_num, lsMkdir)
        fPlot_input1.close()
        get_split_plot(sPlot_input_dir1, lsMkdir)

        os.chdir(sPlot_input_dir2)
        lsMkdir = get_split_dir(nSplitter_num)
        fPlot_input2 = open("Plot_input.txt", 'r')
        Plot_input_split(fPlot_input2, nSplitter_num, lsMkdir)
        fPlot_input2.close()
        get_split_plot(sPlot_input_dir2, lsMkdir)

        os.chdir(sPlot_input_dir3)
        lsMkdir = get_split_dir(nSplitter_num)
        fPlot_input3 = open("Plot_input.txt", 'r')
        Plot_input_split(fPlot_input3, nSplitter_num, lsMkdir)
        fPlot_input3.close()
        get_split_plot(sPlot_input_dir3, lsMkdir)



main()
