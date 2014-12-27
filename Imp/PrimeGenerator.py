def primes(n): 
	if n==2: return [2]
	elif n<2: return []

	odd_set=range(3,n+1,2)	# s is a list of odd numbers between 3 to n+1
	mroot = n ** 0.5		# mroot is the root of n
	half = (n+1)/2-1		# n's half, length of odd_set is almost n's half because it contains only odd numbers
	i = 0
	m = 3					# m is used to point next odd number
	while m <= mroot:		# We only needed to check till the root.
		if odd_set[i] != 0:
			j = ((m*m) - 3)/2 #the trick is here.
			while j < half:
				odd_set[j] = 0 # This is used because we can ignore the non-prime numbers while ilterating.
				j += m
		i = i+1
		m = (2*i)+3
	return [2]+[x for x in odd_set if x]

print primes(13)
print primes(3000)
