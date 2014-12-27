from sys import stdin
from math import floor,ceil
def main():
	T = input()
	tot = []
	for t in range(0,T):
		n,c,m = map(int,stdin.readline().split(' '))
		choc = floor(n/c)
		wrap = choc
		while floor(wrap/m) > 0:
			extra_choc = ceil(wrap/m)
			wrap = wrap%m
			choc+=extra_choc
		tot.append(int(choc))		


	for a in tot:
		print a

main()
