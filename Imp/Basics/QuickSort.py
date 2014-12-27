def quicksort(arr):
	less, equal, greater = [], [], []
	if len(arr) > 1:
		pivot = arr[0]
		for x in arr:
			if x < pivot:
				less.append(x)
			elif x > pivot:
				greater.append(x)
			elif x == pivot:
				equal.append(x)
		a = quicksort(less) + equal + quicksort(greater)
		print ' '.join(map(str,a))
		return a
	else:
		return arr

def main():
	T = input()
	arr = [int(i) for i in raw_input().strip().split()]
	assert len(arr) == T
	quicksort(arr)


main()
