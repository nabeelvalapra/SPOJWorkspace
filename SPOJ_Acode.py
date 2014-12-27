dic = {}
def main():
	while True:
		line = int(raw_input())
		if line == 0:break
		print dp(str(line))
		dic.clear()

def dp(line):
	if line in dic:
		return dic[line]
	else:
		if len(line) > 2:
			a = chk(line[0])*dp(line[1:]) + chk(line[:2])*dp(line[2:])
		elif len(line) > 1:
			a = chk(line[0])*dp(line[1]) + chk(line)
		else:
			a = chk(line)
	dic[line] = a
	return a

def chk(word):
	if word[0] == '0':
		return 0
	if int(word) <= 26 and int(word) > 0:
		return 1
	else:
		return 0

main()
