def main():
	n = int(raw_input())
	arr = []
	while n > 1:
		arr.append(n)
		if n%2 == 0:n/=2
		else:
			n = 3*n+3
		if n in arr:
			print 'NIE'
			break
		if n <= 1:
			print 'TAK'
			break
'''	if n < 1:
		print 'TAK'
	else:
		print 'NIE'
'''
main()
