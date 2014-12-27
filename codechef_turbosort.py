from sys import stdin
def main():
	t = int(raw_input())
	num_list = [stdin.readline().rstrip() for a in range(0,t)]
	num_list = quicksort(list(num_list))
	for _ in num_list:
		print _ 
def quicksort(lst):
	left, right, center = [], [], []
	if len(lst) > 1:
		pivot = int(lst[0])
		for i in range(0,len(lst)):
			num = int(lst[i])
			if pivot > num:
				left.append(num)
			elif pivot < num:
				right.append(num)
			elif pivot == num:
				center.append(num)
		return quicksort(left) + center + quicksort(right)
	else:
		return lst
main()
