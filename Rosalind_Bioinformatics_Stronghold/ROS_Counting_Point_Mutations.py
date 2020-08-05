# Counting Point Mutations
# Given: Two DNA strings of equal length (not exceeding 1 kbp).
# Return: The Hamming distance


def cpm(seq_1, seq_2):
    differences = 0
    for n in range(0, len(seq_1)):
        if seq_1[n] != seq_2[n]:
            differences += 1
    return differences


SEQ_1 = "GAGCCTACTAACGGGAT"
SEQ_2 = "CATCGTAATGACGGCCT"

point_mutations = cpm(SEQ_1, SEQ_2)
print("There are", point_mutations, 'point mutations between the sequences')
