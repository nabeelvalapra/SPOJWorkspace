from sys import stdin
def main():
	T = input()
	result = []
	for t in range(0,T):
		N = input()
		elements = stdin.readline().rstrip().split(' ')
		bingo = False
		set_elements = set(elements)
		if len(set_elements) < len(elements):
			bingo = True
			print 'set working...'
		else:
			for a in elements:
				for b in elements:
					lst = prime(int(a))
					print a,b,lst
					if lst == [] or a == b:
						pass
					else:
						for x in lst:
							if int(b)%x == 0 and int(b) != x:
								bingo = True
								print a,b,lst,'Bingo'								
								break	
				if bingo == True:
					break

		if bingo == True:
			result.append('NO')
		else:
			result.append('YES')
		
	for i in result:
		print i


def prime(x):
	lst = []
	if x == 1:
		pass
	elif x == 2:
		lst.append(x)
	else:
		for i in range(2,x):
			if x%i == 0:
				lst.append(i)
	return lst

main()
