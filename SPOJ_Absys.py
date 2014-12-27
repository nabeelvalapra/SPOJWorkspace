def main():
	out = []
	for _ in range(int(raw_input())):
		space = raw_input()
		if not space:
			pass
		x, y, z = map(str,raw_input().replace('+','').replace('=','').rstrip().split())
		if 'm' in list(z):
			z = int(x) + int(y)
		elif 'm' in list(y):
			y = int(z) - int(x)
		else:
			x = int(z) - int(y)
		out.append(str(x)+' '+'+'+' '+str(y)+' '+'='+' '+str(z))
	for _ in out:
		print _
main()

