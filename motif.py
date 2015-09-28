text = open('vc.txt', 'r').read()
 
import re 
 
print [m.start()+1 for m in re.finditer('(?=ACAATAGAC)', text)]


