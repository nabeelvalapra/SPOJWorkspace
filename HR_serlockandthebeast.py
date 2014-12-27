from math import ceil
def main():
	T = input()
	res = []
	for t in range(T):
		n = input()
		max3 = ceil(n/3)
		max5 = ceil(n/5)
		n_3 = n_5 = numof3 = numof5 = 0
		bingo = 0
		while n_5 <= int(max5):
			while n_3 <= int(max3):
				code = 3*n_3 + 5*n_5
				if code == n:
					numof3 = n_3
					numof5 = n_5
					bingo = 1
					break
				n_3+=1
			if bingo == 1:
				break
			n_5+=1
			n_3 = 0
		if numof3 > 0 or numof5 > 0:
			res.append(str('555'*numof3)+str('33333'*numof5))
		else:	
			res.append('-1')
	for i in res:
		print i	


main()
