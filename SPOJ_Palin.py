def main():
	out = []
	for _ in range(int(raw_input())):
		x = str(int(raw_input()))
		palin = ''
		if len(x)%2 == 0:
			mid = int(len(x)/2) + 1
			right_index = mid
			left_index = mid - 1
		else:
			mid = int(len(x)/2)
			palin = x[mid]
			right_index = mid+1
			left_index = mid-1
		print mid	
		while right_index <= len(x):
			left = int(x[left_index-1])
			right = int(x[right_index-1])
			if right == left:
				pass
			elif right > left:
				palin = str(right) + palin + str(right)
			elif left > right:
				palin = str(left) + palin + str(left)
			right_index+=1
			left_index-=1
		out.append(int(palin))
	for _ in out:
		print _
main()
