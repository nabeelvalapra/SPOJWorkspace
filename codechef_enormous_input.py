from sys import stdin
from itertools import islice
def main():
	n,k = map(int,stdin.readline().split())
	print sum(int(i) % div == 0 for i in islice(stdin,n))

main()
