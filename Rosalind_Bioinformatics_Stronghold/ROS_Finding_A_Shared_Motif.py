#
# Finding A Shared Motif
#
# Given: A collection of k( k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, return any single solution.)
#

from Bio import SeqIO

# Variable init
file = 'rosalind_lcsm.txt'
seqs = []
shortest_length = None
shortest_seq = ''

# Parsing the FASTA file
for seq_record in SeqIO.parse(file, "fasta"):
    seqs.append(str(seq_record.seq))
    if shortest_length is None or shortest_length > len(seq_record):
        shortest_length = len(seq_record)
        shortest_seq = str(seq_record.seq)

# Finding the Motif
motif = ''

for i in range(len(shortest_seq)):
    for j in range(i+1, len(shortest_seq)+1):
        trial = shortest_seq[i:j]
        valid = True
        for s in seqs:
            if not valid:
                break
            if trial in s:
                continue
            else:
                valid = False
        if len(trial) > len(motif) and valid:
            motif = trial

print('The longest shared motif is:')
print(motif)
