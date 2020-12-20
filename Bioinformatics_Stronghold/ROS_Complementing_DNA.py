#Complementing a Strand of DNA

file = open('rosalind_revc.txt')
DNA = file.read()
reverse = ""
for nucl in DNA:
    complement_base = ""
    if nucl == "T":
        complement_base = "A"
    if nucl == "A":
        complement_base = "T"
    if nucl == "C":
        complement_base = "G"
    if nucl == "G":
        complement_base = "C"
    reverse = complement_base + reverse
print(reverse)
    
#Alternate

#st = "AAAACCCGGT"
#st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
#print st
