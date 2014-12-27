def partition(arr):
	l, c, r = [], [], []
	key = arr[0]
	c.append(key)
	for i in range(1,len(arr)):
		if arr[i] > key :
			r.append(arr[i])
		elif arr[i] < key :
			l.append(arr[i])
		elif arr[i] == key :
			c.append(key)
	final_arr = l+c+r
	print ' '.join(map(str,final_arr))






def main():
	n = input()
	arr = [int(i) for i in raw_input().strip().split()]
	assert len(arr) == n
	partition(arr)


main()
