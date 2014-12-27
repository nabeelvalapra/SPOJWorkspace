import sys

def chk(word):
	if word[0] == '0':
		return 0
	if int(word) < 27 and int(word) > 0:
		return 1
	else:
		return 0

def dp(line):
	print line
	if len(line) > 2:
		return chk(line[0])*dp(line[1:]) + chk(line[:2])*dp(line[2:])
	elif len(line) > 1:
		return chk(line[0])*dp(line[1]) + chk(line)
	else:
		return chk(line)

line = sys.stdin.readline().strip()
while line != '0':
	print dp(line) 
	line = sys.stdin.readline().strip()
