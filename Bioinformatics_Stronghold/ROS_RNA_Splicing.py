# RNA Splicing


def parse_fasta(file):
    seqs = []
    strings = file.strip().split('>')
    for file in strings:
        if len(file) == 0:
            continue
        parts = file.split()
        bases = ''.join(parts[1:])
        seqs.append(bases)
    return seqs


def transcribe(dna):
    rna = dna.replace("T", "U")
    return rna


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
    protein = ""
    for nuc in range(0, len(rna), 3):
        codon = rna[nuc:nuc + 3]
        if len(codon) != 3:
            break
        amino = codon_chart[codon]
        if amino == "Stop":
            break
        protein += amino
    return protein


dataset = open('rosalind_splc.txt').read()
results = parse_fasta(dataset)
print(results)

DNA = results[0]
introns = results[1:]

for s in introns:
    DNA = DNA.replace(s, '')

RNA = transcribe(DNA)

for n in range(0, len(RNA)):
    start = RNA[n:n + 3]
    if start == 'AUG':
        ORF = RNA[n:]
        protein_seq = translate(RNA)

print("The processed protein sequence is:")
print(protein_seq)
