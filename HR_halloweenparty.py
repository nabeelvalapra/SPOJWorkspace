from math import ceil,sqrt
from sys import stdin
def main():
	T = int(input())
	results = []
	for a in range(0,T):
		k = input()
		base = int(ceil(float(k/2)))
		bal_k = k - base
		p = base*bal_k
		results.append(p) 
	for i in results:
		print i
main()
