from sys import stdin,stdout
def main():
	out = []
	for _ in range(int(stdin.readline())):
		s = raw_input()
		node = 1
		for i in s:
			if node%2:
				left = int(node)*2
			else:
				left = (int(node)*2)-1
			if i == 'l':
				node = left
			elif i == 'r':
				node = left + 2
		out.append(node%1000000007)
	for _ in out:
		print _	
main()
