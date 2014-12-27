def main():
	out = []
	for i in range(int(raw_input())):
		x = int(raw_input())
		zero = 0
		while x >= 5:
			zero += x/5
			x = x/5
		out.append(zero)
	for i in out:
		print i	

main()
