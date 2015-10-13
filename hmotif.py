##groupby is loading everything as a tuple not a list. The conversion is slow, and I'm trying to figure out how to dix it. I'm about to use biopython at least for fasta parsing. 


from itertools import groupby

with open('rosalind_lcsm.txt') as r:
    strint = groupby(x.strip() for x in r.readlines() if not x.startswith('>'))


def hid_motif(data):
  substrs = lambda x: {x[i:i+j] for i in range(len(x)) for j in range(len(x) - i + 1)}
  s = substrs(data[0])
  for val in data[1:]:
    s.intersection_update(substrs(val))
  return max(s, key=len)

print hid_motif(dnahmotif)



