
##See: https://pypi.python.org/pypi/Counter/1.0.0 for Counter info
## Program counts the number of times each word appears. Currently case sensitive.
 
ci = 'We tried list and we tried dicts also we tried Zen'
 
from collections import Counter
 
counts = Counter(ci.split())
 
print counts
