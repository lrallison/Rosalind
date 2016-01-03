with open ("dna.txt", "r") as myfile:
    data=myfile.readlines()
    mRNA = data

def next_transcript(mRNA, cur_pos):
    initial=mRNA            .find("AUG", cur_pos)
    for i in range(initial, len(mRNA),3):
        if mRNA[i:i+3] == "UAG":
            return initial, i

map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def print_translation(mRNA, start, end):
    newseq = ""
    for i in range(start, end, 3):
        key = mRNA[i:i+3]
        newseq = newseq + map[key]
    print(newseq)

cur_pos = 0
while 1:
    start, end = next_transcript(mRNA, cur_pos)
    if start == -1:
        break
    print_translation(mRNA, start, end)
    cur_pos = end
