import time
import os
start_time = time.time()

def measured_time(t) :
    # t = time.time() - start_time
    print( "measured time : {0} m {1} s".format( int(t // 60), round( (t % 60), 2 ) ) )


def file_list() :
    path_dir = "D:\\NGS_data\\software\\miRPlant_V6\\build_bwt_idx_v32\\genome\\Mpo_miR"
    lsFile = os.listdir(path_dir)
    print(len(lsFile))
    print(lsFile[0])
    # delete .tmp file
    for i in range(0, len(lsFile)) :
        if "tmp" in lsFile[i] :
            os.remove(path_dir + "\\" + lsFile[i])

    
def main() :
    file_list()

file_list()
