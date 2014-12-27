from sys import stdin
def main():
	T = input()
	arr = stdin.readline().rstrip().split(' ')
	arr = [int(x) for x in arr]
	assert len(arr) == T
	ins_sort(arr)
	
def ins_sort(arr):
	counter = 0
	for i in range(0,len(arr)):
		key = arr[i]
		j = i -1
		while j >= 0 and arr[j] > key : 
			arr[j+1] = arr[j]
			j-=1
			counter+=1
		arr[j+1] = key
	print counter
	print arr
main()
