# Open Reading Frame Problem


# function to get unique ORFs
def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def transcribe(dna):
    rna = dna.replace("T", "U")
    return rna


def reverse_comp(s):
    complement = s
    complement = complement.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
    return complement


# Translates RNA to Protein, and checks for stop codon
def translate(rna):
    codon_chart = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                   "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                   "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
                   "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
                   "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                   "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                   "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                   "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                   "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                   "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                   "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                   "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                   "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                   "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                   "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                   "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }
    flag = True
    protein = ""
    for nuc in range(0, len(rna), 3):
        codon = rna[nuc:nuc + 3]
        if len(codon) != 3:
            break
        amino = codon_chart[codon]
        if amino == "Stop":
            flag = False
            break
        protein += amino
    return protein, flag


# Load in seq from file
file = open('rosalind_orf.txt', 'r').read()
parts = file.split()
title = parts[0]
bases = ''.join(parts[1:])
print('Sample Name:', title)
seq = bases

# Create reverse complement
reverse = reverse_comp(seq)

# Create the Reading Frames
first = seq
second = seq[1:]
third = seq[2:]
fourth = reverse
fifth = reverse[1:]
sixth = reverse[2:]

reading_frames = [first, second, third, fourth, fifth, sixth]

# Initialize candidate list
candidate_proteins = []

# Cycles through all reading frames to find ORFs
for rf in reading_frames:
    RNA = transcribe(rf)
    for n in range(0, len(RNA), 3):
        start = RNA[n:n+3]
        if start == 'AUG':
            ORF = RNA[n:]
            potential_protein, bad = translate(ORF)
            if bad:
                continue
            candidate_proteins.append(potential_protein)

# Check for duplicates
candidate_proteins = unique(candidate_proteins)

# Print out all candidate proteins
print('\nCandidate Proteins:')
for p in candidate_proteins:
    print(p)
