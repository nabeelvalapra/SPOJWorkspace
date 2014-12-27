from sys import stdin,stdout
def main():
	n, m = map(int,stdin.readline().rstrip().split())
	lst = map(int,stdin.readline().rstrip().split())
	assert n == len(lst)
	for _ in range(m):
		cmd = stdin.readline().rstrip()
		pointer = cmd[0]
		if pointer == 'R':
			stdout.write(str(lst[int(cmd[2:]) -1]))
			stdout.write('\n')
		elif pointer == 'A':
			x, i = int(cmd[2:]), 0
			while i < x:
				lst.insert(0,lst.pop())
				i+=1
		elif pointer == 'C':
			x, i = int(cmd[2:]), 0
			while i < x:
				lst.append(lst.pop(0))
				i+=1

main()
