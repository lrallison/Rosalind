##http://rosalind.info/problems/gc/

text = open('gc.txt', 'r').read()


print lambda text: sum([100.0 for base in text if base in ('G', 'C')])/len(seq)
