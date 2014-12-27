def main():
	out = []
	def fact(a):return a*fact(a-1) if a>0 else 1
	for i in range(int(raw_input())):
		out.append(fact(int(raw_input())))
	for i in out:
		print i
main()
