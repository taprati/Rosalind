from Bio import ExPASy
from Bio import SwissProt
handle = ExPASy.get_sprot_raw('B5ZC00') #you can give several IDs separated by commas
record = SwissProt.read(handle)         #use SwissProt.parse for multiple proteins

bio_process = []
for item in record.cross_references:
    if item[0] == 'GO' and item[2][0]=='P':
        bio_process.append(item[2].lstrip('P:'))

print('\n'.join(bio_process))
      
