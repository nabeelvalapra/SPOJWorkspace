def main():
	out = []
	for _ in range(10):
		apples = int(raw_input())
		dif = int(raw_input())
		down, up = 0, 0
		status = apples%2
		if status == 0:
			mid = apples/2
			down, up = mid-dif/2, mid+dif/2
		else:
			mid = apples/2 +1
			dif-=1
			down, up = mid-1-dif/2, mid+dif/2
		out.append(up)
		out.append(down)
	for i in out:
		print i

main()

