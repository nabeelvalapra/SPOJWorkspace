def main():
	out = []
	for _ in range(int(raw_input())):
		x, y = map(int,raw_input().split())
		point = findElement(x,y)
		out.append(point)
	for _ in out:
		print _ 

def findElement(x,y):
	if y not in [x,x-2]:return 'No Number'
	elif x%2 == 0:
		if y == x:return x+x
		else:return x+x-2
	else:
		if y == x:return x+x-1
		else:return x+x-3

main()
