from sys import stdin
def insertionsort(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j = i -1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1] = key
	return arr	

def quicksort(arr):					
	left ,right ,center = [], [], []
	if len(arr) > 1:
		pivot = arr[0]
		for x in arr:
			if x > pivot:
				right.append(x)
			elif x < pivot:
				left.append(x)
			elif x == pivot:
				center.append(x)
		a = quicksort(left) + center + quicksort(right)
		return a
	else:
		return arr


def main():
	n,k = map(int,stdin.readline().strip().split())
	arr = map(int,stdin.readline().strip().split())
	assert len(arr) == n 
	sorted_arr = quicksort(arr)
	total_cost,counter = 0,0
	for x in sorted_arr:
		total_cost += int(x)
		if total_cost > k:
			break
		counter += 1
	print counter
main()

