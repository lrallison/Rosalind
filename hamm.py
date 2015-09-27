# Python has a distance package with a built in calculator. 
# https://pypi.python.org/pypi/Distance/0.1
# NumPy can do it easily as well
# Below is a proof of concept

##Problem

#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

#Return: The Hamming distance dH(s,t).

s= 'GAGCCTACTAACGGGAT'
t= 'CATCGTAATGACGGCCT'

def hamm(s, t):
	#check to see if they're the same length
	assert len(s) == len(t)
	return sum(ch1 != ch2 for ch1, ch2 in zip(s, t))

print hamm(s,t)


