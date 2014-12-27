def main():
	T = int(input())
	for t in range(0,T):
		num = int(input())
		digs = list(str(num))
		counter = 0
		for dig in digs:
			if int(dig) == 0:
				pass
			elif num%int(dig) == 0:
				counter+=1
		print counter



main()
