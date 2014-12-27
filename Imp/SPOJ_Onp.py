def main():
	out = []
	for _ in range(int(raw_input())):
		expr = raw_input()
		out.append(convert(expr))
	for _ in out:
		print _ 

def convert(expr):
	out, operator = [], []
	for char in expr:
		if char.isalpha():
			out.append(char)
		elif char in ['+','-','*','/','^']:
			operator.append(char)
		elif char == ')':
			out.append(operator.pop())
	return ''.join(out)

main()
