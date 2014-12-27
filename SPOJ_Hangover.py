def main():
	out = []
	while True:
		x = float(raw_input())
		if x == 0.00:
			break
		p = 1.0/2
		counter = 1
		i = 3
		while p <= x:
			p+=1.0/i
			counter+=1
			i+=1
		out.append(counter)
	for _ in out:
		print _,'card(s)' 
	
main()
