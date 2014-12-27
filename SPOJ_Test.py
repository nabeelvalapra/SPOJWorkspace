from sys import stdin
def main():
	out = []
	while True:
		x = input()
		if int(x) == 42:
			break
		else:
			out.append(x)	
	for x in out:
		print x
main()
