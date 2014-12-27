from sys import stdin
'''
Heapify checks its two 'roots', if 'root' is bigger than the 'point',
it swaps the values, and Heapify checks the swapped value and it 
gets down unit it reachs the 'end'.
'''
def heapify(end,point,lst):
	left = 2*point + 1
	right = 2 * (point + 1)
	biggest = point
	if left < end and lst[point] < lst[left] :
		biggest = left
	if right  < end and lst[biggest] < lst[right] :
		biggest = right
	if point != biggest :
		lst[point], lst[biggest] = lst[biggest], lst[point]
		swapped_point = biggest
		heapify(end,swapped_point,lst)	

def heapsort(lst):
	end = len(lst)
	head = end/2 - 1

	for point in range(head,-1,-1):
		heapify(end,point,lst)
	'''
	First element is swapped to the 'last_index'.
	The 'heap.length' is reduced [there is difference between 'heap.length' 
	and 'array.length'].
	Heapify is called to maintain the Heap structure. 
	'''
	for last_index in range(end-1,0,-1):
		lst[last_index],lst[0] = lst[0],lst[last_index]
		heapify(last_index,0,lst)

def main():
	lst = map(int,stdin.readline().strip().split())
	heapsort(lst)
	print lst

main()
