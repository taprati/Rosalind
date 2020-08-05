# Consensus and Profile

# input
data = open('consensus_profile_seqs.txt').read()
strings = data.strip().split('>')
sequences = []
for s in strings:
    if len(s) == 0:
        continue
    name_seq = s.split()
    name = name_seq[0]
    seq = ''.join(name_seq[1:])
    sequences.append(seq)

# Making Profile
N = len(sequences)
bp = len(sequences[0])
print('There are',N,'Sequences')
print('They are',bp,'Bp long')










    

