# Locating Restriction Sites


def reverse_comp(s):
    complement = s
    complement = complement.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    return complement


# Load in seq from file
file = open('rosalind_revp.txt', 'r').read()
parts = file.split()
title = parts[0]
bases = ''.join(parts[1:])
print('Sample Name:', title)
seq = bases

# Test Seq
# seq = 'TCAATGCATGCGGGTCTATATGCAT'

# Initialize list of position length pairs
pos_len = []

# Find Sites
print(len(seq))
for length in range(4, 12+1):
    for pos in range((len(seq)-length)+1):
        s = seq[pos:pos+length]
        r = reverse_comp(s)
        if s == r:
            pair = (pos, length)
            pos_len.append(pair)

# Prints out Restriction Sites
print('\nPalindromic Sites:')
for p in pos_len:
    print(p[0]+1, p[1])
