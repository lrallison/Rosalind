##From stepic: https://stepic.org/lesson/Hidden-Messages-in-the-Replication-Origin-2/step/6?course=Bioinformatics-Algorithms&unit=401
##CODE CHALLENGE: Implement PatternCount (reproduced below).
     ##Input: Strings Text and Pattern.
     ##Output: Count(Text, Pattern).
##Though I solved it entirely differently
 
import re 
 
text = open('dataset.txt', 'r').read()
  
print len(re.findall("(?=CGCG)", text))
