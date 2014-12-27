def insertion_sort(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j = i -1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j = j - 1
		arr[j+1] = key #'j+1' is used because in the above step j's value is decreased by one
		print ' '.join(map(str,arr))


def main():
	T = input()
	arr = [int(i) for i in raw_input().strip().split()]
	assert len(arr) == T
	insertion_sort(arr)
	


main()
