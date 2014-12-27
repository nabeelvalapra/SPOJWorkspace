from sys import stdin
def quicksort(arr):
	if len(arr) > 1:
		pivot = arr[0]
		right, left, center = [], [], []
		for i in arr:
			if i > pivot:
				right.append(i)
			elif i < pivot:
				left.append(i)
			elif i == pivot:
				center.append(i)
		return quicksort(left) + center + quicksort(right)
	else:
		return arr

def main():
	T = input()
	for i in range(0,T):
		n, k = map(int,stdin.readline().rstrip().split())
		A = map(int,stdin.readline().rstrip().split())
		B = map(int,stdin.readline().rstrip().split())
		A = quicksort(A)
		B = quicksort(B)
		print A, B
		i, j = 0, len(B)-1
		bingo = True
		while j >= 0 and i < len(B):
			AB = A[i] + B[j]
			if AB >= k:
				i += 1
				j -= 1
			else:
				bingo = False
				break
		if bingo:
			print 'YES'
		else:
			print 'NO'			

main()
