
n= input('Number of generations?')
k= input('Size of litters?')


def fibunnies(n, k):
#returns the number of rabbits after n generations with k sized litters
	rabbits = [0,1]
	for i in xrange(n-1):	
		rabbits[i % 2] = rabbits[(i-1) % 2] + k*rabbits[i % 2] 	
	return max(rabbits)


print fibunnies(n,k)	
	
