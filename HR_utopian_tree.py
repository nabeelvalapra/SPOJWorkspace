from sys import stdin
def main():
	T = input()
	results = []
	for i in range(0,T):
		a = stdin.readline().rstrip()
		results.append(pro(a))

	for result in results:
		print result
def pro(num):
	value = 1
	for a in range(0,int(num)):
		if a%2==0 :
			value += 1
		else:
			value *= 2
	return value

main()
