dnahmotif = open('hm.txt', 'r').read

def hid_motif(data):
  substrs = lambda x: {x[i:i+j] for i in range(len(x)) for j in range(len(x) - i + 1)}
  s = substrs(data[0])
  for val in data[1:]:
    s.intersection_update(substrs(val))
  return max(s, key=len)

print hid_motif(dnahmotif)
