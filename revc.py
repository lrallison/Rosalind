dnarc = open('dnarc.txt', 'r').read()

import string

dna_chars = "ACGT"
rev_chars = "TGCA"

revc = string.maketrans(dna_chars,rev_chars)

print dnarc.translate(revc)[::-1]





