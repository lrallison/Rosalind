##CODE CHALLENGE: Solve the Pattern Matching Problem (restated below).
 
##Pattern Matching Problem: Find all occurrences of a pattern in a string.
     ##Input: Two strings, Pattern and Genome.
     ##Output: All starting positions where Pattern appears as a substring of Genome.
 
##Sample Input:
     ##ATAT
     ##GATATATGCATATACTT
 
##Sample Output:
     ##1 3 9
## http://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python
 
text = open('vc.txt', 'r').read()
 
import re 
 
print [m.start() for m in re.finditer('ATAT', text)]
