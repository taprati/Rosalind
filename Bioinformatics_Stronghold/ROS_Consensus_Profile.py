#
# Consensus and Profile
#


def nuc_count(seqs):
    length = len(seqs[0])
    nseqs = len(seqs)

    profile = [ [ None for i in range(length)] for j in range(nseqs)]
    for n in range(length):
        A = 0
        C = 0
        G = 0
        T = 0
        


# input data
file = open("Data/rosalind_test.txt","r")

seqs = []
current_seq = ""
for line in file:
    l = line.strip("\n")
    if l[0]  != ">":
        current_seq += l
    else:
        if current_seq != "":
            seqs.append(current_seq)
            current_seq = ""
seqs.append(current_seq)

nuc_count(seqs)









    

