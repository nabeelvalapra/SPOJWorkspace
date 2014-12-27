from math import pow
def main():
	out = []
	for _ in range(int(raw_input())):
		a, b = map(int,raw_input().rstrip().split())
		if b == 0:
			out.append(1)
		else:	
			b = b%4
			if b == 0:
				b = 4
			c = a**b
			digit = c%10
			out.append(digit)
	for i in out:
		print i
	

main()
