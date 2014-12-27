from sys import stdin 
def main():
	for _ in range(int(raw_input())):
		size = int(raw_input())
		sum_lst, _sum = [], 0
		for __ in range(size):
			line = map(int,stdin.readline().rstrip().split())
			for i in line:
				_sum += i
			sum_lst.append(_sum)
			_sum = 0
		print max(sum_lst), sum_lst


main()
