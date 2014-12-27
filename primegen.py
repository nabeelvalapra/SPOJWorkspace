def primes(n,low=1):
	'''return a list of prime numbers between LOW and N'''
	low = low / 2 * 2 + 1   # convert LOW to odd number
	lNum = range(low,n+1,2) # create a list of all the odd numbers between LOW and N
	iRoot= n ** 0.5
	iMid = len(lNum)        # number of numbers in the list
	i = 0
	m = 3                   # 2 is removed from the list because we didn't include the even numbers, so we start with removing
							# the 3 multiples (9,15,21 ....)
	while m < iRoot:
		if lNum[i] != 0:      # if we haven't removed the number and its multiplies already
								# I don't like this line, I think it might work in the original algorithm, but might make this one skip
								# some numbers. If it does skip numbers, remove this 'if' statement
			j = (m*m - low) / 2   # j is the _index_ of the first multiple of m to remove
			while (j<iMid):
				if (j >= 0):        # ignore indexes below zero (for obvious reasons)
					lNum[j] = 0
					j+=m
	
			i += 1
			m += 2

	return [x for x in lNum if x != 0]

primes(31)
