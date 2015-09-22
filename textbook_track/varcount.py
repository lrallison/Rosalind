##From https://stepic.org/lesson/Hidden-Messages-in-the-Replication-Origin-2/step/9?course=Bioinformatics-Algorithms&unit=401
##CODE CHALLENGE: Solve the Frequent Words Problem.
     ##Input: A string Text and an integer k.
     ##Output: All most frequent k-mers in Text.
 
Text= open('varinput.txt','r').read()
inter= input('Length of k?')
vardict = {}
 
 
for i in range(len(Text)-inter):
    var = Text[i:i+inter]
    if var not in vardict:
            vardict[var] = 0
    else: 
        vardict[var] += 1
 
for count in vardict: 
    if vardict[count] == max(vardict.values()):
        print count
