text = 'AGCTGATAGTTAGCCTCCATGGAAAGTACTGCTACAGTATGCCGTAACGGTTTCAAGAAGCACTTATCAGCTAGGATATAGGTCTACTCCCGGGCCGTTGATTTAATTACAATTTATACAGTATTAATCGAAAGGTCGCTTCGGGCATGTATAGAATGGTCTTCTAGCATGGCCGCGCGTCCACCACACGTACGCCGATAATTTAGTATGACGAGGGTGAGTCGTTAAGGACCAAGTATAGCGAAAGAACTGACCATCTGTTTTCGGCCCGGTAGGTAGATCTGCTTAGCCGTGTGCACTTGACCAGACAGTGAGTAAGCGTGGGCTGAGTCCAACTAACCAGCCGAGGAATTCGTAACGCGACCGTATCGTGCGCCTTGGGATAAGGCAGACGAACCTCATGATGAAATGCATGCCGTTCGCGTAACGCCAGCATTTAATACGGACTGCAAGGCCTATCATACTTTGACCGATCAGGCCAATAGCGCCACCTTGCCGGTTTTAACAATAACGTCTAACCACTTGAACTCTGTATTTCTCATAAACTGGAGCGAATGGTTAAACGTCTTATGTAGTGAATTTCGTCGGGCTACGATTCACTAATCAACGTCAAGTGTATCTTAACAGTGCGTCGCCGAAAAGTGTTGTTCTATCAAACCCAACCTTGCCGTAATAACTCAAATTCAACCGTTGAAGGAATTTAATCGAGCGCGAACGCAGAGTCGGTCGCTGGCCGTTGAGTGTGTGAAACGATTGCAGGCCTGAGGCCCGTTGCCAGTCAGTCTCTCCACGCATGACATACTTGCATTACCCAATAGGACCGTATCCCCATCGTGTTCGAAGACGATAGGAGTTCCCTATGCTTGCTCACCAGAACTCCACGACAAACGAAC'
 
from collections import Counter

def count_m(text):
    count = Counter(text)
    return count['A'], count['C'], count['G'], count['T']
	
print count_m(text)
