def main():
	out = []
	for _ in range(int(raw_input())):
		space = raw_input()
		stud = int(raw_input())
		_sum = 0
		for __ in range(stud):
			_sum += input()
		if _sum%stud == 0:
			out.append('YES')
		else:
			out.append('NO')
	
	for _ in out:
		print _
main()
