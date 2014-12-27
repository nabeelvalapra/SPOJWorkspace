def main():
	out = []
	for _ in range(int(raw_input())):
		n = input()
		if n%2 == 0:
			num = ((n/2)-1)*500 + 442
		else:
			num = (n/2)*500 + 192
		out.append(num)
	for _ in out:
		print _
		
main()
