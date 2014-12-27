from math import ceil
def main():
	out = []
	for _ in range(10):
		n = raw_input()
		if n == '':
			break
		else:
			n = int(n)
		_max = find(n)
		out.append(_max)
	for _ in out:
		print _
dic = {0:0}
def find(n):
	a, b, c = int(ceil(n/2)), int(ceil(n/3)), int(ceil(n/4))
	tot = a + b + c
	if tot <= n:
		return n
	else:	
		if tot in dic:
			return dic[tot]
		else:
			dic[tot] = find(a) + find(b) + find(c)
			return dic[tot]
main()	
