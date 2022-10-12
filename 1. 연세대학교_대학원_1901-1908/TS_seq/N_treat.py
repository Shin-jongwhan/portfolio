def N_treat(seq) :
    seq_range = [0, 1]       #initialization
    lsSepa_seq = []     #initialization
    for i in range(0, len(seq) ) :
        if i == 0 :
            if seq[i] == "N" :
                seq_range = [1, 2]
            else : continue
        elif i < (len(seq) - 1) and i > 0 :
            if seq[i] != "N" :
                if seq[i - 1] == "N" :
                    seq_range = [i, i + 1]
                else :
                    seq_range[1] = i + 1
                if seq[i + 1] == "N" :
                    seq_range[1] = i + 1
                    lsSepa_seq.append(seq_range)
                else : continue
            elif seq[i] == "N" :
                if seq[i + 1] == "N" :
                    continue
                else :
                    seq_range = [i + 1, i + 2]
        elif i == ( len(seq) - 1 ) :
            if seq[i] == "N" :
                continue
            else :
                if seq[i - 1] == "N" :
                    seq_range = [i, i + 1]
                    lsSepa_seq.append(seq_range)
                else :
                    seq_range[1] = i + 1
                    lsSepa_seq.append(seq_range)
    print(seq)
    print(lsSepa_seq)
    #seq check
    new_seq = ""
    for i in lsSepa_seq :
        new_seq = new_seq + "".join(seq[ i[0] : i[1] ])
    print(new_seq)
    print()

# test
seq = "NNNAAAAACCCNACTNNN"
seq2 = "AAANANCCNNAACACACANNA"
N_treat(seq)
N_treat(seq2)
