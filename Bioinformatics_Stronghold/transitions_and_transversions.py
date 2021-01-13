#
# Transitions and Transversions
#
# A <-> G or C <-> T == Transition
#  All else = transversion
#


def tt_ratio(s1, s2):
    transitions = 0
    transversions = 0
    transition_map = { "A":"G", "G":"A","C":"T","T":"C"}

    for n in range(0, len(s1)):
        if s1[n] != s2[n]:
            if transition_map[s1[n]] == s2[n]:
                transitions += 1
            else:
                transversions += 1
    ratio = transitions / transversions
    return ratio


# input data
file = open("Data/rosalind_tran.txt","r")

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

# Run tt_ratio
tt = tt_ratio(seqs[0],seqs[1])
print(tt)


