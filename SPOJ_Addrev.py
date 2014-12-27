from sys import stdin
def main():
	T = input()
	out = []
	for i in range(0,T):
		x, y = map(int,stdin.readline().strip().split())
		x, y = reverse(x), reverse(y)
		z = reverse(x+y)
		out.append(z)
	for i in out:
		print i 

def reverse(a):
	out_str = str()
	while a > 0:
		num = a % 10
		out_str+=str(num)
		a = a/10
		print out_str
	return int(out_str)
main()
