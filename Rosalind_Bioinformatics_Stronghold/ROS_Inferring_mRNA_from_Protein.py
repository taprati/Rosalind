# Inferring mRNA from Protein

file = open('rosalind_mrna.txt', 'r').read()

protein = file

# Test
# Protein = 'MA'
# Should be 12

six = ['L', 'R', 'S']
fours = ['V', 'P', 'T', 'A', 'G']
threes = ['I']
twos = ['F', 'Y', 'H', 'Q', 'N', 'K', 'D', 'E', 'C']
ones = ['W', 'M']

combo = 1
for n in range(1, len(protein)):
    if protein[n] in six:
        combo *= 6
    elif protein[n] in fours:
        combo *= 4
    elif protein[n] in threes:
        combo *= 3
    elif protein[n] in twos:
        combo *= 2
    elif protein[n] in ones:
        combo *= 1

# There are 3 possible stop codons
combo *= 3

print(combo % 1000000)


# Another Way to do it
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
datafile = open('rosalind_mrna.txt', 'r')
prot = datafile.read()
number = 1
for aa in prot:
        number *= amino_acids.count(aa)
print((number * amino_acids.count('*')) % 1000000)