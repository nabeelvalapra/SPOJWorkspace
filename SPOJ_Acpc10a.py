from sys import stdin
def main():
	out = []
	while True:
		x, y, z = map(int,stdin.readline().rstrip().split())
		if x == 0 and y == 0 and z == 0:break
		dif = y-x
		div = 0 if x == 0 or y == 0 else y/x 
		if z == y+dif:
			out.append('AP '+str(z+dif))
		elif z == y*div:
			out.append('GP '+str(z*div))
	for _ in out:
		print _
main()
